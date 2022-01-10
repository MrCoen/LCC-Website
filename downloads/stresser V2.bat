@echo off
setlocal enableextensions enabledelayedexpansion
    set /a "x = 0"

    
:more_to_process
if %x% leq 30 (
        echo %x%
        set /a "x = x + 1"
        start stress.py
        goto :more_to_process

    )

