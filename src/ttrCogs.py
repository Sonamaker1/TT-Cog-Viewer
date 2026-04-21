def os_path_join(*in_args):
    return "/".join(in_args)
    

RESOURCES_DIR = "resources"


# ***************** COG SUIT TEXTURES ***************

TTR_SELLBOT_BLAZER = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "s_blazer.jpg")
TTR_CASHBOT_BLAZER = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "m_blazer.jpg")
TTR_LAWBOT_BLAZER = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "l_blazer.jpg")
TTR_BOSSBOT_BLAZER = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "c_blazer.jpg")

TTR_SELLBOT_ARM = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "s_sleeve.jpg")
TTR_CASHBOT_ARM = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "m_sleeve.jpg")
TTR_LAWBOT_ARM = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "l_sleeve.jpg")
TTR_BOSSBOT_ARM = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "c_sleeve.jpg")

TTR_SELLBOT_LEG = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "s_leg.jpg")
TTR_CASHBOT_LEG = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "m_leg.jpg")
TTR_LAWBOT_LEG = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "l_leg.jpg")
TTR_BOSSBOT_LEG = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "c_leg.jpg")

TTR_WAITER_SUIT = os_path_join(RESOURCES_DIR, "phase_12", "maps", "ttcc_ene_suittex_waiter.png")

TTR_SUIT_MODEL_C_HEADS = os_path_join(RESOURCES_DIR, "phase_3.5", "models", "char", "ttr_r_ene_cgc_heads.bam")
TTR_SUIT_MODEL_B_HEADS = os_path_join(RESOURCES_DIR, "phase_4", "models", "char", "ttr_r_ene_cgb_heads.bam")
TTR_SUIT_MODEL_A_HEADS = os_path_join(RESOURCES_DIR, "phase_4", "models", "char", "ttr_r_ene_cga_heads.bam")


TTR_SUIT_MODEL_DICT = {
    "ttra": os_path_join(RESOURCES_DIR, "phase_3.5", "models", "char", "ttr_r_ene_cga_suit.bam"),
    "ttrb": os_path_join(RESOURCES_DIR, "phase_3.5", "models", "char", "ttr_r_ene_cgb_suit.bam"),
    "ttrc": os_path_join(RESOURCES_DIR, "phase_3.5", "models", "char", "ttr_r_ene_cgc_suit.bam"),
}
    
TTR_SUIT_MODEL_NAMES = {
    "ttra": "Buff (TTR)",
    "ttrb": "Thin (TTR)",
    "ttrc": "Fat (TTR)",
}

TTR_SELLBOT = {
    "**/torso":   TTR_SELLBOT_BLAZER,
    "**/arms":    TTR_SELLBOT_ARM,
    "**/legs":    TTR_SELLBOT_LEG,
}

TTR_CASHBOT = {
    "**/torso":   TTR_CASHBOT_BLAZER,
    "**/arms":    TTR_CASHBOT_ARM,
    "**/legs":    TTR_CASHBOT_LEG,
}

TTR_LAWBOT = {
    "**/torso":   TTR_LAWBOT_BLAZER,
    "**/arms":    TTR_LAWBOT_ARM,
    "**/legs":    TTR_LAWBOT_LEG,
}

TTR_BOSSBOT = {
    "**/torso":   TTR_BOSSBOT_BLAZER,
    "**/arms":    TTR_BOSSBOT_ARM,
    "**/legs":    TTR_BOSSBOT_LEG,
}



departmentSell= {
    "emblem": "emblem_sales",
    "tParts": TTR_SELLBOT,
    "suitTex": TTR_SELLBOT["**/torso"],
    "dept": "s"
}

departmentCash= {
    "emblem": "emblem_money",
    "tParts": TTR_CASHBOT,
    "suitTex": TTR_CASHBOT["**/torso"],
    "dept": "m"
}

departmentLaw = {
    "emblem": "emblem_legal",
    "tParts": TTR_LAWBOT,
    "suitTex": TTR_LAWBOT["**/torso"],
    "dept": "l"
}

departmentBoss = {
    "emblem": "emblem_corporate",
    "tParts": TTR_BOSSBOT,
    "suitTex": TTR_BOSSBOT["**/torso"],
    "dept": "c"
}

TTR_COG_C_DATA = {
    "headTextureModel": "resources/phase_3.5/models/char/ttr_m_ene_cgc_heads_textures.bam",
    "head": TTR_SUIT_MODEL_C_HEADS,
    "name": "ttr_r_ene_cgc_heads",
    "bodyname": "ttrc",
}

TTR_COG_B_DATA = {
    "headTextureModel": "resources/phase_4/models/char/ttr_m_ene_cgb_heads_textures.bam",
    "head": TTR_SUIT_MODEL_B_HEADS,
    "name": "ttr_r_ene_cgb_heads",
    "bodyname": "ttrb",
}


TTR_COG_A_DATA = {
    "headTextureModel": "resources/phase_4/models/char/ttr_m_ene_cga_heads_textures.bam",
    "head": TTR_SUIT_MODEL_A_HEADS,
    "name": "ttr_r_ene_cga_heads",
    "bodyname": "ttra",
}

def MAKECOG(department, bodytype, headCog, textureNode, scale, colorTuple):
    return {
        "hands": colorTuple,
        "scale": scale,
        "cog": headCog,
        "headTextureName": textureNode,
        "name": bodytype["name"],
        "head": bodytype["head"],
        "headTextureModel": bodytype["headTextureModel"],
        "suit": bodytype["bodyname"],
        "suitTex": department["suitTex"],
        "texture_parts": department["tParts"],
        "dept": department["dept"],
        "emblem": department["emblem"],
        "suitToggle": "y",
    }


aSize = 6.06
bSize = 5.29
cSize = 4.14

corpPolyColor = (0.95, 0.75, 0.75, 1.0)
legalPolyColor = (0.75, 0.75, 0.95, 1.0)
moneyPolyColor = (0.65, 0.95, 0.85, 1.0)
salesPolyColor = (0.95, 0.75, 0.95, 1.0)

color = (242 / 255, 242 / 255, 1, 1)
scale = 0.96618

#Dictionary of Size and Colors
DSC = {
    'cc':[3.5 / cSize, (0.55, 0.65, 1.0, 1.0), (0.25, 0.35, 1.0, 1.0)], #coldcaller
    'tm':[3.75 / bSize, salesPolyColor], #telemarketer
    'nd':[4.35 / aSize, salesPolyColor], #name-dropper
    'gh':[4.75 / cSize, salesPolyColor], #gladhander
    'ms':[4.75 / bSize, salesPolyColor], #movershaker
    'tf':[5.25 / aSize, salesPolyColor], #twoface
    'm':[5.75 / aSize, salesPolyColor], #mingler
    'mh':[7.0 / aSize, salesPolyColor], #mr-hollywood

    'sc':[3.6 / cSize, moneyPolyColor], #shortchange
    'pp':[3.55 / aSize, (1.0, 0.5, 0.6, 1.0)], #pennypincher
    'tw':[4.5 / cSize, moneyPolyColor], #tightwad
    'bc':[4.4 / bSize, moneyPolyColor], #beancounter
    'nc':[5.25 / aSize, moneyPolyColor], #numbercruncher
    'mb':[5.3 / cSize, moneyPolyColor], #moneybags
    'ls':[6.5 / bSize, (0.5, 0.85, 0.75, 1.0)], #loanshark
    'rb':[7.0 / aSize, moneyPolyColor], #robber-baron
    
    'bf':[4.0 / cSize, legalPolyColor], #bottom-feeder
    'b':[4.375 / bSize, (0.95, 0.95, 1.0, 1.0)], #bloodsucker
    'dt':[4.25 / aSize, legalPolyColor], #doubler-talker
    'ac':[4.35 / bSize, legalPolyColor], #ambulancechaser
    'bs':[4.5 / aSize, legalPolyColor], #backstabber
    'sd':[5.65 / bSize, (0.5, 0.8, 0.75, 1.0)], #spin-doctor
    'le':[7.125 / aSize, (0.25, 0.25, 0.5, 1.0)], #legaleagle
    'bw':[7.0 / aSize, legalPolyColor], #bigwig
    
    'f': [4.0 / cSize, corpPolyColor],   #flunky
    'p': [3.35 / bSize, corpPolyColor], #pencilpusher
    'ym':[4.125 / aSize, corpPolyColor], #yesman
    'mm':[2.5 / cSize, corpPolyColor], #micromanager
    'ds':[4.5 / bSize, corpPolyColor], #downsizer
    'hd':[6.5 / aSize, corpPolyColor], #headhunter
    'cr':[6.75 / cSize, (0.85, 0.55, 0.55, 1.0)], #corporate-raider
    'tbc':[7.0 / aSize, (0.75, 0.95, 0.75, 1.0)], #bigcheese
}



TTR_COG_DATA = {
    "TTR Cold Caller": MAKECOG( departmentSell, TTR_COG_C_DATA, "coldcaller", None, DSC['cc'][0], DSC['cc'][1]),
    "TTR Short Change": MAKECOG( departmentCash, TTR_COG_C_DATA, "coldcaller", None, DSC['sc'][0], DSC['sc'][1]),
    "TTR Bottom Feeder": MAKECOG( departmentLaw, TTR_COG_C_DATA, "tightwad", "**/bottom-feeder", DSC['bf'][0], DSC['bf'][1]),
    "TTR Flunky": MAKECOG( departmentBoss, TTR_COG_C_DATA, "flunky", None, DSC['f'][0], DSC['f'][1]),

    "TTR Telemarketer": MAKECOG( departmentSell, TTR_COG_B_DATA, "telemarketer", None, DSC['tm'][0], DSC['tm'][1]),
    "TTR Penny Pincher": MAKECOG( departmentCash, TTR_COG_A_DATA, "pennypincher", None, DSC['pp'][0], DSC['pp'][1]),
    "TTR Bloodsucker": MAKECOG( departmentLaw, TTR_COG_B_DATA, "movershaker", "**/blood-sucker", DSC['b'][0], DSC['b'][1]),
    "TTR Pencil Pusher": MAKECOG( departmentBoss, TTR_COG_B_DATA, "pencilpusher", None, DSC['p'][0], DSC['p'][1]),

    "TTR Name Dropper": MAKECOG( departmentSell, TTR_COG_A_DATA, "numbercruncher", "**/name-dropper", DSC['nd'][0], DSC['nd'][1]),
    "TTR Tightwad": MAKECOG( departmentCash, TTR_COG_C_DATA, "tightwad", None, DSC['tw'][0], DSC['tw'][1]),
    "TTR Double Talker": MAKECOG( departmentLaw, TTR_COG_A_DATA, "twoface", "**/double-talker", DSC['dt'][0], DSC['dt'][1]),
    "TTR Yesman": MAKECOG( departmentBoss, TTR_COG_A_DATA, "yesman", None, DSC['ym'][0], DSC['ym'][1]),

    "TTR Glad Hander": MAKECOG( departmentSell, TTR_COG_C_DATA, "gladhander", None, DSC['gh'][0], DSC['gh'][1]),
    "TTR Bean Counter": MAKECOG( departmentCash, TTR_COG_B_DATA, "beancounter", None, DSC['bc'][0], DSC['bc'][1]),
    "TTR Ambulance Chaser": MAKECOG( departmentLaw, TTR_COG_B_DATA, "ambulancechaser", None, DSC['ac'][0], DSC['ac'][1]),
    "TTR Micromanager": MAKECOG( departmentBoss, TTR_COG_C_DATA, "micromanager", None, DSC['mm'][0], DSC['mm'][1]),

    "TTR Mover & Shaker": MAKECOG( departmentSell, TTR_COG_B_DATA, "movershaker", None, DSC['ms'][0], DSC['ms'][1]),
    "TTR Number Cruncher": MAKECOG( departmentCash, TTR_COG_A_DATA, "numbercruncher", None, DSC['nc'][0], DSC['nc'][1]),
    "TTR Back Stabber": MAKECOG( departmentLaw, TTR_COG_A_DATA, "backstabber", None, DSC['bs'][0], DSC['bs'][1]),
    "TTR Downsizer": MAKECOG( departmentBoss, TTR_COG_B_DATA, "beancounter", None, DSC['ds'][0], DSC['ds'][1]),

    "TTR Two-Face": MAKECOG( departmentSell, TTR_COG_A_DATA, "twoface", None, DSC['tf'][0], DSC['tf'][1]),
    "TTR Money Bags": MAKECOG( departmentCash, TTR_COG_C_DATA, "moneybags", None, DSC['mb'][0], DSC['mb'][1]),
    "TTR Spin Doctor": MAKECOG( departmentLaw, TTR_COG_B_DATA, "telemarketer", "**/spin-doctor", DSC['sd'][0], DSC['sd'][1]),
    "TTR Head Hunter": MAKECOG( departmentBoss, TTR_COG_A_DATA, "headhunter", None, DSC['hd'][0], DSC['hd'][1]),

    "TTR The Mingler": MAKECOG( departmentSell, TTR_COG_A_DATA, "twoface", "**/mingler", DSC['m'][0], DSC['m'][1]),
    "TTR Loan Shark": MAKECOG( departmentCash, TTR_COG_B_DATA, "loanshark", None, DSC['ls'][0], DSC['ls'][1]),
    "TTR Legal Eagle": MAKECOG( departmentLaw, TTR_COG_A_DATA, "legaleagle", None, DSC['le'][0], DSC['le'][1]),
    "TTR Corporate Raider": MAKECOG( departmentBoss, TTR_COG_C_DATA, "tightwad", "**/corporate-raider", DSC['cr'][0], DSC['cr'][1]),

    "TTR Mr. Hollywood": MAKECOG( departmentSell, TTR_COG_A_DATA, "yesman", None, DSC['mh'][0], DSC['mh'][1]),
    "TTR Robber Baron": MAKECOG( departmentCash, TTR_COG_A_DATA, "yesman", "**/robber-baron", DSC['rb'][0], DSC['rb'][1]),
    "TTR Big Wig": MAKECOG( departmentLaw, TTR_COG_A_DATA, "bigwig", None, DSC['bw'][0], DSC['bw'][1]),
    "TTR The Big Cheese": MAKECOG( departmentBoss, TTR_COG_A_DATA, "bigcheese", None, DSC['tbc'][0], DSC['tbc'][1]),
}

TTR_COG_DATA["TTR Cold Caller"]["headColor"] = DSC['cc'][2]
TTR_COG_DATA["TTR Flunky"]["unhide"] = ["glasses"]

"""
{
    "TTR Bottom Feeder": MAKECOG(
        departmentLaw, 
        TTR_COG_C_DATA,
        "tightwad",
        "**/bottom-feeder",
        (191 / 255, 191 / 255, 242 / 255, 1),
        0.96618
    ),
    "TTR Bloodsucker": MAKECOG(
        departmentLaw, 
        TTR_COG_B_DATA,
        "movershaker",
        "**/blood-sucker",
        (242 / 255, 242 / 255, 1, 1),
        0.83521504950495049504950495049505
    )
}
"""
