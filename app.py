from moralis import sol_api
import json

api_key = "<MORALIS-API>"
network = "mainnet"

def getParams():
    address = input("your wallet address: ")
    return address

def getNfts(network, address):
    params = {"network":network, "address":address}
    result = sol_api.account.get_nfts(api_key=api_key, params=params)
    return result

def getMetadata(network, mint):
    params = {"network":network, "address":mint}
    result = sol_api.nft.get_nft_metadata(api_key=api_key, params=params)
    return result

def prettifier(key, value):
    return f"{key}: {value}"

def mintsLister(network):
    mints = []
    for nft in getNfts(network, getParams()):
        mints.append(nft["mint"])
    return mints

def showData(network, mints):
    for mint in mints:
        datas = getMetadata(network, mint)
        for key, value in datas.items():
            if key != "metaplex":
                print(prettifier(key, value))
            else:
                print(key.upper())
                for key, value in value.items():
                    if key != "owners":
                        print("    " + prettifier(key, value))
                    else:
                        print(key.upper())
                        for owner in value:
                            print("    ", end="")
                            print(owner)

showData(network, mintsLister(network))
