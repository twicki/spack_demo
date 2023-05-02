import subprocess
import warnings


def geos_check():
    try:
        geos_version = subprocess.check_output(['geos-config', '--version'])
        geos_version = tuple(int(v) for v in geos_version.split(b'.')
                         if 'dev' not in str(v))
    except (OSError, ValueError, subprocess.CalledProcessError):
        warnings.warn('Unable to determine GEOS version')
        exit(1)
    else:
        if geos_version < (3,0,0):
            print("incompatible geos found")
            exit(1)
        else:
            print(f"found geos {geos_version}")