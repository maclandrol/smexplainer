from typing import Union
import os
import fsspec
import datamol as dm

NOTEBOOK_AVAILABLE = False
try:
    from IPython.core.display import Image, SVG

    NOTEBOOK_AVAILABLE = True

except ImportError:
    pass


def _format_smarts(smarts: Union[str, dm.Mol], ignore_error: bool = False):
    """Format a molecular pattern"""
    with dm.without_rdkit_log():
        smarts_mol = None
        if isinstance(smarts, str):
            smarts_mol = dm.from_smarts(smarts)
        elif isinstance(smarts, dm.Mol):
            smarts_mol = smarts
            smarts = dm.to_smarts(smarts_mol)
        if smarts_mol is None and not ignore_error:
            raise ValueError("Invalid smarts")
        elif smarts_mol is None:
            smarts = None
    return smarts


def _save_image(image, output: Union[str, os.PathLike]):
    """Save image to output

    Args:
        image: input image
        output: output file
    """
    with fsspec.open(output, "wb") as OUT:
        OUT.write(image)


def _nb_display(content, format: str = "png"):
    """Prepare image for display in notebook

    Args:
        content: content of the image
        format (str, optional): format of the image. Defaults to "png".
    """
    out = content
    if isinstance(out, (SVG, Image)):
        return out
    if not NOTEBOOK_AVAILABLE:
        return out
    if format == "png":
        out = Image(data=content)
    elif format == "svg":
        out = SVG(data=content)
    return out


def is_notebook():
    try:
        from IPython import get_ipython

        cur_ipython = get_ipython()
        if "IPKernelApp" not in cur_ipython.config:  # pragma: no cover
            raise ImportError("console")
        elif cur_ipython.__class__.__name__ not in [
            "ZMQInteractiveShell",
            "google.colab._shell",
        ]:
            raise ImportError("console")

    except:
        return False
    else:  # pragma: no cover
        return True
