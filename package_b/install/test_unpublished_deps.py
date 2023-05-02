def unpublished():
    try:
        import package_a
    except ImportError as e:
        raise RuntimeError("Dependency on package_a not found") from e
