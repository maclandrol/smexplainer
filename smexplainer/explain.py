from typing import Optional
from typing import Union
from typing import List
import os
import datamol as dm
from functools import partial
from requests_toolbelt import sessions
from . import _utils as utils

SESSION = sessions.BaseUrlSession(base_url="https://smarts.plus/smartsview/")


def batch_explain(smarts_list: List[str], output_folder: Union[str] = None, **kwargs):
    """Batch explain a list of smarts

    Args:
        smarts_list: list of input smarts
        output_folder (Union[str], optional): [description]. Defaults to None.

    """
    kwargs.pop("outfile", None)
    kwargs["ignore_error"] = True
    format = kwargs.get("filetype", "png")
    output = dm.parallelized(partial(explain, **kwargs), smarts_list)
    if output_folder is not None:
        for i, out in enumerate(output):
            outfile = dm.utils.fs.join(output_folder, f"{i}.{format}")
            utils._save_image(out, outfile)

    if utils.is_notebook():
        output = [utils._nb_display(out, format=format) for out in output]
    return output


def explain(
    smarts: Union[str, dm.Mol],
    comparesmarts: Optional[str] = None,
    vmode: Optional[int] = 0,
    vbonds: Optional[int] = 1,
    textdesc: Optional[bool] = True,
    depsymbols: Optional[bool] = True,
    smartsheading: Optional[bool] = True,
    trim: Optional[bool] = True,
    labels: Optional[bool] = True,
    cmode: int = 4,
    detectarom: Optional[bool] = True,
    smileslikearom: Optional[bool] = True,
    filetype: Optional[str] = "png",
    outfile: Optional[Union[str, os.PathLike]] = None,
    ignore_error: bool = False,
):
    """Explain or compare two smarts

    Args:
        smarts: a smarts string (valid) to visualize
        comparesmarts: optional smarts to compare agains
        vmode: visualization Mode:
            * 0 = Complete visualization (Default)
            * 1 = ID-Mapping
            * 2 = Element symbols
            * 3 = Structure Diagram-Like
        vbonds: Visualization of Default Bonds
            * 0 = "Single bonds"
            * 1 = "Single or Aromatic Bonds" (default)
        textdesc: Legend Option 1: Textual desciption. Default is True
        depsymbols: Legend Option 2: Depiction of SMARTS symbols. Default is True
        smartsheading: Legend Option 3: Write SMARTS as picture heading. Default is True
        trim: SMARTS trim active. Default is True.
        labels: Show Atom Labels. Default is False.
        cmode: Compare Mode: This only affects compare images
            * 1 = Search for Identical Patterns
            * 2 = Subset search from smarts
            * 3 = Subset search from comparesmarts
            * 4 = Similarity Search (Default)
        detectarom: Detect Aromatic Bonds. Default to True.
        smileslikearom: SMILES-like Aromaticity Detection. Default ot True
        filetype: Output File Type ("png", "svg" or "pdf"). Default to png
        outfile: Optional Output file where to save the output image
        ignore_error: Whether to silently ignore errors
    """
    smarts = utils._format_smarts(smarts, ignore_error=ignore_error)
    params = dict(
        smarts=smarts,
        vmode=int(vmode),
        vbonds=int(vbonds),
        textdesc=int(textdesc),
        depsymbols=int(depsymbols),
        smartsheading=int(smartsheading),
        trim=int(trim),
        labels=int(labels),
        detectarom=int(detectarom),
        cmode=int(cmode),
        smileslikearom=int(smileslikearom),
        filetype=filetype,
    )

    input_error = False
    if comparesmarts is not None:
        comparesmarts = utils._format_smarts(comparesmarts, ignore_error=ignore_error)
        input_error = False
        params["comparesmarts"] = comparesmarts

    input_error = smarts is None or input_error
    if input_error and ignore_error:
        return None
    elif input_error:
        raise ValueError("Invalid input smarts !")
    r = SESSION.get("download_rest/", params=params)
    out = r.content
    if outfile:
        utils._save_image(out, outfile)
    if utils.is_notebook():
        out = utils._nb_display(out, format=filetype)
    return out
