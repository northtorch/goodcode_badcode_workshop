#!/bin/sh
TARGET_PYTHON_VERSION=3.11.3
echo "${TARGET_PYTHON_VERSION}"

echo '===== check python version ====='
CURRENT_PYTHON_VERSION=`pyenv latest -q ${TARGET_PYTHON_VERSION}`
if [ -n "${CURRENT_PYTHON_VERSION}" ]; then
    # インストール済みのPythonバージョンが存在する
    echo "found ${CURRENT_PYTHON_VERSION}"
else
    # インストール済みのPythonバージョンが存在しない
    # pyenvで最新をインストールする
    echo "PYTHON VERSION ${TARGET_PYTHON_VERSION} not found."
    LATEST_VERSION=`pyenv latest -k -q ${TARGET_PYTHON_VERSION}`
    echo "INSTALL: ${LATEST_VERSION}"
    pyenv install ${LATEST_VERSION}
    CURRENT_PYTHON_VERSION=${LATEST_VERSION}
fi
echo "USE: ${CURRENT_PYTHON_VERSION}"

echo '===== make venv ====='
poetry config virtualenvs.in-project true
pyenv local ${CURRENT_PYTHON_VERSION}
poetry env use ${CURRENT_PYTHON_VERSION}
poetry install --no-root
