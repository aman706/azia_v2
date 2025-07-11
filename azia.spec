# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['azia_main.py'],
    pathex=[],
    binaries=[],
    datas=[
        ('models/vosk-model-small-en-us-0.15', 'models/vosk-model-small-en-us-0.15'),
        ('models/llm/mistral.gguf', 'models/llm'),
        ('memory/memory.json', 'memory'),
        ('journal/empathy_dataset.txt', 'journal'),
        ('assets/azia_icon.ico', 'assets')
    ],
    hiddenimports=[
        'pyttsx3.drivers',
        'pyttsx3.drivers.espeak',
        'pyttsx3.drivers.sapi5',
        'pyttsx3.drivers.nsss',
    ],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Azia',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    icon='assets/azia_icon.ico'  # Optional icon
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Azia'
)
