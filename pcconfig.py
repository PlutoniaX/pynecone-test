import pynecone as pc

class PywebappConfig(pc.Config):
    pass

config = PywebappConfig(
    app_name="py_webapp",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)
