import logging
from typing import Optional

from zimp.simplification.builder import SimplificationStrategy, build_simplifier
from zimp.simplification.simplifier import BaseSimplifier

from experiment.config import Config


def build_simplifier_from_cfg(config: Config) -> Optional[BaseSimplifier]:
    if config is None or config.zimp_mechanism is None:
        return None

    s_strategy = get_simpl_strategy(config.zimp_mechanism)
    kwargs = config.zimp_config or {}
    return build_simplifier(s_strategy, **kwargs)


def get_simpl_strategy(cfg_string: str) -> SimplificationStrategy:
    try:
        return SimplificationStrategy(cfg_string)
    except ValueError as e:
        logging.error(f'Unknown config.zimp_mechanism value of {cfg_string}', e)
        raise e
