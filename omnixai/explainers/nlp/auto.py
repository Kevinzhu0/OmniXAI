#
# Copyright (c) 2022 salesforce.com, inc.
# All rights reserved.
# SPDX-License-Identifier: BSD-3-Clause
# For full license text, see the LICENSE file in the repo root or https://opensource.org/licenses/BSD-3-Clause
#
from typing import Collection, Callable, Any, Dict

from ...data.text import Text
from ..base import AutoExplainerBase


class NLPExplainer(AutoExplainerBase):
    """
    The class derived from `AutoExplainerBase` for text data,
    allowing users to choose multiple explainers and generate
    different explanations at the same time.

    .. code-block:: python

        explainer = NLPExplainer(
            explainers=["shap"],
            mode="classification",
            model=model,
            preprocess=preprocess_function,
            postprocess=postprocess_function
        )
        local_explanations = explainer.explain(x)
    """

    _MODELS = AutoExplainerBase._EXPLAINERS[__name__.split(".")[2]]

    def __init__(
        self,
        explainers: Collection,
        mode: str,
        model: Any,
        data: Text = Text(),
        preprocess: Callable = None,
        postprocess: Callable = None,
        params: Dict = None,
    ):
        """
        :param explainers: The names or alias of the explainers to use.
        :param mode: The task type, e.g. classification or regression.
        :param model: The machine learning model which can be a scikit-learn model,
            a tensorflow model, a torch model, or a prediction function.
        :param data: The training data used to initialize explainers.
            It can be empty, e.g., `data = Text()`, for those explainers such as
            `LIME` and `SHAP` that don't require training data.
        :param preprocess: The preprocessing function that converts the raw data
            into the inputs of ``model``.
        :param postprocess: The postprocessing function that transforms the outputs of ``model``
            to a user-specific form, e.g., the predicted probability for each class.
        :param params: A dict containing the additional parameters for initializing each explainer,
            e.g., `params["lime"] = {"param_1": param_1, ...}`.
        """
        super().__init__(
            explainers=explainers,
            mode=mode,
            data=data,
            model=model,
            preprocess=preprocess,
            postprocess=postprocess,
            params=params,
        )