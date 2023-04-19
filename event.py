from enum import Enum

class ChanceEvent(Enum):
    MARKET_CRUSH = -300
    POLICY_SUPPORT = 300
    STRONG_COMPETEPOT = -200
    COOPERATE = 200
    TECH_CRUSH = -100
    TECH_SUPPORT = 100

class TaxEvent(Enum):
    MARKET_TAX = -30
    REVENUE_TAX = -20
    REALEASTATE_TAX = -10
    