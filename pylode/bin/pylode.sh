#!/bin/bash
PARENT="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
GRANDPARENT=`dirname $PARENT`
GREATGRANDPARENT=`dirname $GRANDPARENT`
"$GREATGRANDPARENT/venv/bin/python" "$GRANDPARENT/cli.py" "$@"
