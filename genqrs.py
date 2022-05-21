import qrcode


nfts = {
    "Angel 088":"https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/1375222676491770976886489731613262964940696994594946997516756248885723136001",
    "Interlinked":"https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/1375222676491770976886489731613262964940696994594946997516756245587188252673",
    "NonoIm":"https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/37113267255361574183604483851777514579287633297905833288271730274457840779265",
    "SMILE13":"https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/37113267255361574183604483851777514579287633297905833288271730297547584962561",
    "EnchantedFae1093":"https://opensea.io/assets/0xf4bf7c9b229f1b8728001349918196b344ace80f/522",
    "EnchantedFae1102":"https://opensea.io/assets/0xf4bf7c9b229f1b8728001349918196b344ace80f/413",
    "GLORY":"https://makersplace.com/ivgallery/glory-1-of-1-185819/",
    "Golden":"https://opensea.io/assets/0xc0b4777897a2a373da8cb1730135062e77b7baec/158",
    "KRSK12021SABET":"https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/1320647387308535254427024482131342257786249516275092859116706453057383170101",
    "Fallen_Venus":"https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/113880553193085112553003971177710328279102620484568317680388881656330181410817",
    "Laer_Eyez":"https://opensea.io/assets/0x495f947276749ce646f68ac8c248420045cb7b5e/113880553193085112553003971177710328279102620484568317680388881657429693038593",
    "Reaching Out":"https://foundation.app/@supafray/foundation/79843",
    "Desert Nyghts":"https://rarible.com/token/0xd07dc4262bcdbf85190c01c996b4c06a461d2430:254403?tab=owners",
    "Romanzowave":"https://objkt.com/asset/hicetnunc/674056",
    "NYCHOSTHEROLLER":"https://opensea.io/assets/matic/0x2953399124f0cbb46d2cbacd8a89cf0599974963/44858638403891452300550604988499869153051560781699280910881726789232338403772",
    "MoodieNo042":"https://knownorigin.io/gallery/8000000-moodie-no-042",
    "repop3":"https://app.stargaze.zone/launchpad",
    "repop41":"https://app.stargaze.zone/launchpad",
    "repop58":"https://app.stargaze.zone/launchpad",
    "repop71":"https://app.stargaze.zone/launchpad",
    "bk993":"https://app.stargaze.zone/launchpad/stars1gc5wcdn9ges00w0l2cfxd7r2puyflak5dmkg26rsh083afmnrjxqu7sutd",
    "bk1027":"https://app.stargaze.zone/launchpad/stars1gc5wcdn9ges00w0l2cfxd7r2puyflak5dmkg26rsh083afmnrjxqu7sutd",
    "bk1061":"https://app.stargaze.zone/launchpad/stars1gc5wcdn9ges00w0l2cfxd7r2puyflak5dmkg26rsh083afmnrjxqu7sutd",
    "bk1536":"https://app.stargaze.zone/launchpad/stars1gc5wcdn9ges00w0l2cfxd7r2puyflak5dmkg26rsh083afmnrjxqu7sutd",
    "anyo9":"https://app.stargaze.zone/launchpad/stars1ywpctek72gsccmr8gjgaamzs8vhh7ju3sjtvwk82daafavw5u0es293t0m",
    "anyo10":"https://app.stargaze.zone/launchpad/stars1ywpctek72gsccmr8gjgaamzs8vhh7ju3sjtvwk82daafavw5u0es293t0m",
    "anyo15":"https://app.stargaze.zone/launchpad/stars1ywpctek72gsccmr8gjgaamzs8vhh7ju3sjtvwk82daafavw5u0es293t0m",
    "anyo23":"https://app.stargaze.zone/launchpad/stars1ywpctek72gsccmr8gjgaamzs8vhh7ju3sjtvwk82daafavw5u0es293t0m",
    "anyo25":"https://app.stargaze.zone/launchpad/stars1ywpctek72gsccmr8gjgaamzs8vhh7ju3sjtvwk82daafavw5u0es293t0m",  
    "shut01":"https://app.stargaze.zone/launchpad/stars1m95chyen8tqrawmjhxrewcwscg5vj8pkxzxeaw8em7fnjwth8rusaftwk4",
    "shut02":"https://app.stargaze.zone/launchpad/stars1m95chyen8tqrawmjhxrewcwscg5vj8pkxzxeaw8em7fnjwth8rusaftwk4",
    "shut03":"https://app.stargaze.zone/launchpad/stars1m95chyen8tqrawmjhxrewcwscg5vj8pkxzxeaw8em7fnjwth8rusaftwk4", 
    "choad6377":"https://nitter.moomoo.me/starchoadz",
    "choad6367":"https://nitter.moomoo.me/starchoadz"


}   
for nft in nfts:
    img = qrcode.make(nfts[nft])
    img.save("static/" +nft + ".png")
    print("Saving {}".format(nft))