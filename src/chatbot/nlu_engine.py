import io
import os
from snips_nlu import SnipsNLUEngine
from snips_nlu.dataset import Dataset
from snips_nlu.default_configs import CONFIG_ES


class NLUEngine:
    def __init__(
        self, engine_path, dataset_path, language="en", seed=42, config=CONFIG_ES
    ):
        self.engine_path = engine_path
        self.dataset_path = dataset_path
        self.seed = seed
        self.language = language
        self.config = config

        if self.engine_exist():
            self.load_engine()
        else:
            self.fit_dataset()
            self.save_engine()

    def engine_exist(self):
        return os.path.exists(self.engine_path)

    def fit_dataset(self):
        with io.open(self.dataset_path) as f:
            dataset = Dataset.from_yaml_files("es", [f])
            self.nlu_engine = SnipsNLUEngine(config=self.config, random_state=self.seed)
            self.nlu_engine.fit(dataset)

    def save_engine(self):
        self.nlu_engine.persist(self.engine_path)

    def load_engine(self):
        self.nlu_engine = SnipsNLUEngine.from_path(self.engine_path)

    def predict(self, text):
        return self.nlu_engine.parse(text)
