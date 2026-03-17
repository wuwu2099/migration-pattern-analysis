@ECHO OFF
@SET PYTHONIOENCODING=utf-8
@SET PYTHONUTF8=1
@FOR /F "tokens=2 delims=:." %%A in ('chcp') do for %%B in (%%A) do set "_CONDA_OLD_CHCP=%%B"
@chcp 65001 > NUL
@CALL "C:\Users\Home_Computer\anaconda3\condabin\conda.bat" activate "d:\Wu\2026\Project Portfolio\migration-pattern-analysis\.conda"
@IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
@"d:\Wu\2026\Project Portfolio\migration-pattern-analysis\.conda\python.exe" -Wi -m compileall -q -l -i C:\Users\Home_Computer\AppData\Local\Temp\tmp9uhfreda -j 0
@IF %ERRORLEVEL% NEQ 0 EXIT /b %ERRORLEVEL%
@chcp %_CONDA_OLD_CHCP%>NUL
