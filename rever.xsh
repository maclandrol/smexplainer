# Configuration

$PROJECT = $GITHUB_REPO  = 'smexplainer'
$GITHUB_ORG = 'maclandrol'
$PUSH_TAG_REMOTE = 'git@github.com:maclandrol/smexplainer.git'

# Logic

$AUTHORS_FILENAME = 'AUTHORS.rst'
$AUTHORS_METADATA = '.authors.yml'
$AUTHORS_SORTBY = 'alpha'
$AUTHORS_MAILMAP = '.mailmap'

$CHANGELOG_FILENAME = 'CHANGELOG.rst'
$CHANGELOG_TEMPLATE = 'TEMPLATE.rst'
$CHANGELOG_NEWS = 'news'

$PYPI_BUILD_COMMANDS = ['sdist']
$PYPI_UPLOAD = True

$ACTIVITIES = ['check', 'authors', 'changelog', 'version_bump', 'tag', 'push_tag', 'ghrelease', 'pypi']

$VERSION_BUMP_PATTERNS = [('smexplainer/_version.py', r'__version__\s*=.*', "__version__ = \"$VERSION\""),
                          ('setup.py', r'version\s*=.*,', "version=\"$VERSION\",")
                          ]
