import os
import pytest

def test_env_image_exists():
    directory = "week13"
    filenames = ["env.png", "env.jpg", "env.jpeg"]
    found = any(os.path.isfile(os.path.join(directory, fname)) for fname in filenames)
    assert found, f"No environment image (env.png/jpg/jpeg) found in the '{directory}' directory"