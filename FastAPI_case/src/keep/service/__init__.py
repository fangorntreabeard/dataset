from fastapi import APIRouter


from curen import currency
# from provider import ProviderRouter as Pr

main_router = APIRouter()
main_router.include_router(currency.CurrencyRouter.router)
# main_router.include_router(Pr.router)
# main_router.include_router(Pr.router)
