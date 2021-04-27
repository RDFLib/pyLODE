# -*- mode: python ; coding: utf-8 -*-
## run `pyinstaller pylode-cli.spec` to create `dist/pylode.exe` dist
## note it requires pywin32

block_cipher = None

a = Analysis(
            ['cli.py'],
            pathex=['.'],
            binaries=[],
            datas=[
               ('templates','templates'),
               ('style','style')
            ],
            hiddenimports=[                
                'urllib3',
                'rdflib',
                'rdflib.namespace',
                'rdflib.plugins',
                'rdflib_jsonld',
                'rdflib_jsonld.serializer'
                'pylode.common',
                'pylode.profiles'
            ],
            hookspath=[],
            runtime_hooks=[],
            excludes=[],
            win_no_prefer_redirects=False,
            win_private_assemblies=False,
            cipher=block_cipher,
            noarchive=False
)

pyz = PYZ(
            a.pure,
            a.zipped_data,
            cipher=block_cipher
)

exe = EXE(
            pyz,
            a.scripts,
            a.binaries,
            a.zipfiles,
            a.datas,
            [],
            name='pylode',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            upx_exclude=[],
            runtime_tmpdir=None,
            console=True
)
