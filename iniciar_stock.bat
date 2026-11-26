@echo off
chcp 65001 > nul
title Sistema de Stock - Artículos de Computación
cd /d "%~dp0"

echo Iniciando Sistema de Stock...
echo.

:: Verifica si 'python' esta disponible; si no, intenta con el lanzador 'py' de Windows
where python >nul 2>nul
if %errorlevel% equ 0 (
    python main.py
) else (
    where py >nul 2>nul
    if %errorlevel% equ 0 (
        py main.py
    ) else (
        echo [ERROR] No se encontro Python instalado o agregado al PATH del sistema.
        echo Asegurate de tener Python instalado y vuelve a intentarlo.
    )
)

echo.
pause