# YOLOR
This fork is just a packaged version of [github.com/WongKinYiu/yolor](https://github.com/WongKinYiu/yolor) (which is the implementation of the paper [You Only Learn One Representation: Unified Network for Multiple Tasks](https://arxiv.org/abs/2105.04206))

Install using `pip install git+https://github.com/marcinwrochna/yolor.git`

Usage:
```python
from yolor_mimsolutions.models.models import Darknet
from yolor_mimsolutions.utils.datasets import letterbox
...
```

The scripts can be run from the module as well, for example:
```bash
python -m yolor_mimsolutions train --batch-size 32 \
                                   --img 960 960 \
                                   --name ${RUN_NAME} \
                                   --data ${DATASET}/dataset_config.yaml \
                                   --cfg yolor_p6.cfg \
                                   --hyp hyp.scratch.1280.yaml \
                                   --weights '' \
                                   --device 7 \
                                   --epochs 300
```
Files like `yolor_p6.cfg` or `hyp.scratch.1280.yaml` are then retrieved from inside the package (or you can provide your own).
