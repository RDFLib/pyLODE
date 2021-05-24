# -*- mode: python ; coding: utf-8 -*-
## run `pyinstaller pyLODE-cli.spec` to create `dist/pylode.exe` dist
## note it requires pywin32

block_cipher = None

a = Analysis(
            ['cli.py'],
            pathex=['.'],
            binaries=[
            ],
            datas=[
                ('style/*.css', 'style' ),
                ('templates/*', 'templates' )
            ],
            hiddenimports=[
                'rdflib',
                'urllib3',
                'validators',
                'rdflib.plugins',
                'rdflib.plugins.memory',
                'rdflib.plugins.parsers.notation3',
                'rdflib.plugins.serializers.turtle',
                'rdflib.plugins',
                'rdflib.serializer',
                'rdflib.serializer.Serializer',
                'rdflib_jsonld',
                'rdflib_jsonld.serializer',
                'rdflib_jsonld.parser',
                'win32com.gen_py',
                'pkg_resources.py2_warn'
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
            Tree('templates', prefix='templates'),
            a.zipfiles,
            a.datas,
            [],
            name='pyLODE',
            debug=False,
            bootloader_ignore_signals=False,
            strip=False,
            upx=True,
            upx_exclude=[],
            runtime_tmpdir=None,
            console=True
)
