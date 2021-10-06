#!/bin/bash

echo "installing brew.."

bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

echo "installing powershell using brew.."

brew install --cask powershell

echo "loading powershell.."

pwsh