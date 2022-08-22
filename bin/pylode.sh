#!/bin/bash
PARENT=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
GRANDPARENT=`dirname $PARENT`
"$GRANDPARENT/.venv/bin/python" "$GRANDPARENT/pylode/cli.py" "$@"
