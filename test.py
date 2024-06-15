import mwapi
from revscoring import Model
from revscoring.extractors.api.extractor import Extractor
import enchant
from pyenchant_utils import EnchantStr, UTF16EnchantStr
import time
import argparse
import logging

logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)

parser = argparse.ArgumentParser()
parser.add_argument("model_binary_path", help="The path to the model binary to use")
parser.add_argument("rev_id", type=int, help="The wiki revision-id to score")
parser.add_argument("wiki", help="The target wiki shortname (example: en, vi, es, it, etc..")
args = parser.parse_args()

# monkey patching enchant to support older binaries. There are some older models
# which have been trained with older enchant binaries. By including additional classes from v2.0.0
# of the pyenchant library (the pyenchant_utils.py file), we allow these models to be loaded and used.
enchant.utils.UTF16EnchantStr = UTF16EnchantStr
enchant.utils.EnchantStr = EnchantStr

with open(args.model_binary_path) as f:
    scorer_model = Model.load(f)

extractor = Extractor(mwapi.Session(host=f"https://{args.wiki}.wikipedia.org",
                                    user_agent="revscoring test elukey github"))

print("Extracting features..")
start = time.perf_counter()
feature_values = list(extractor.extract(args.rev_id, scorer_model.features))
end = time.perf_counter()
total = end - start
print(f"Took {total:.4f} seconds")

print("Scoring..")
print(scorer_model.score(feature_values))
