# Universal Scene Description

## Dependencies

1. For C++
    - CMAKE version >= 3.12
    - GCC (Optional)
2. For Python 2.x
    - PySide or PySide2
    - PyOpenGL

### Optional for Python 3.6

Install same dependencies for python but upper version and this [USD for 3.6](https://developer.nvidia.com/usd) project from NVidia

## USD

If you use python version 2.x, you need use this [instructions](https://github.com/PixarAnimationStudios/USD) for installing.

### After installing all options, you need extend environment variables for linux:

```bash
    export USDPATH=/usr/local/USD
    export PATH=$USDPATH/bin:$PATH
    export PYTHONPATH=$USDPATH/lib/python:$PYTHONPATH
```

### After this you can see results:

```bash
    usdview USD/extras/usd/tutorials/convertingLayerFormats/Sphere.usda
```
