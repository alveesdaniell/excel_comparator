# cli.spec

# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['excel_comparator/cli.py'],
    pathex=['/Users/danielalves/Repositorios/excel_comparator'],
    binaries=[],
    datas=[
    ('/Library/Frameworks/Python.framework/Versions/3.13/lib/python3.13/site-packages/streamlit-1.44.1.dist-info/*', 'streamlit-1.44.1.dist-info'),
    ('excel_comparator/app.py', '.'),  # <- Correção aqui
    ],
    hiddenimports=[
        'streamlit',
        'importlib_metadata',
        'streamlit.server.server',  # Exemplo de submódulo do streamlit
        'streamlit.runtime',        # Exemplo de submódulo do streamlit
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
    name='excel_comparator',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    runtime_tmpdir=None,
    console=True,
    icon=None,  # Se você tiver um ícone, pode adicionar aqui
)

# Output diretório, para garantir que os arquivos vão para a pasta 'dist'
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    name='excel_comparator'
)
