import requests, time

def sniper_evm(chain: str):
    print(f"Снайпер новых пар на {chain.capitalize()} (GeckoTerminal API)...")
    seen = set()
    while True:
        r = requests.get(f"https://api.geckoterminal.com/api/v2/networks/{chain}/new_pools?limit=10")
        for pool in r.json()["data"]:
            addr = pool["id"]
            if addr in seen: continue
            seen.add(addr)
            token = pool["attributes"]["base_token_symbol"]
            price = float(pool["attributes"]["base_token_price_usd"])
            if price < 0.0001:  # ультра-лоу кап
                print(f"СНАЙП!\n"
                      f"{token} на {chain.upper()}\n"
                      f"Цена: ${price:.10f}\n"
                      f"Ликвидность: ${float(pool['attributes']['reserve_in_usd']):,.0f}\n"
                      f"https://www.geckoterminal.com/{chain}/pools/{pool['attributes']['address']}\n"
                      f"{'-'*50}")
        time.sleep(4)

if __name__ == "__main__":
    chain = input("Chain (ethereum/base/solana/arbitrum): ").lower()
    sniper_evm(chain)
