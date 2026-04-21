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

def MAKECOG(department, bodytype, headCog, textureNode, colorTuple, scale):
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

color = (242 / 255, 242 / 255, 1, 1)
scale = 0.96618

TTR_COG_DATA = {
    "TTR Cold Caller": MAKECOG( departmentSell, TTR_COG_C_DATA, "coldcaller", None, color, scale),
    "TTR Short Change": MAKECOG( departmentCash, TTR_COG_C_DATA, "coldcaller", None, color, scale),
    "TTR Bottom Feeder": MAKECOG( departmentLaw, TTR_COG_C_DATA, "tightwad", "**/bottom-feeder", (191 / 255, 191 / 255, 242 / 255, 1), 0.96618),
    "TTR Flunky": MAKECOG( departmentBoss, TTR_COG_C_DATA, "flunky", None, color, scale),

    "TTR Telemarketer": MAKECOG( departmentSell, TTR_COG_B_DATA, "telemarketer", None, color, scale),
    "TTR Penny Pincher": MAKECOG( departmentCash, TTR_COG_A_DATA, "pennypincher", None, color, scale),
    "TTR Bloodsucker": MAKECOG( departmentLaw, TTR_COG_B_DATA, "movershaker", "**/blood-sucker", (242 / 255, 242 / 255, 1, 1), 0.83521504950495049504950495049505),
    "TTR Pencil Pusher": MAKECOG( departmentBoss, TTR_COG_B_DATA, "pencilpusher", None, color, scale),

    "TTR Name Dropper": MAKECOG( departmentSell, TTR_COG_A_DATA, "numbercruncher", "**/name-dropper", color, scale),
    "TTR Tightwad": MAKECOG( departmentCash, TTR_COG_C_DATA, "tightwad", None, color, scale),
    "TTR Double Talker": MAKECOG( departmentLaw, TTR_COG_A_DATA, "twoface", "**/double-talker", color, scale),
    "TTR Yesman": MAKECOG( departmentBoss, TTR_COG_A_DATA, "yesman", None, color, scale),

    "TTR Glad Hander": MAKECOG( departmentSell, TTR_COG_C_DATA, "gladhander", None, color, scale),
    "TTR Bean Counter": MAKECOG( departmentCash, TTR_COG_B_DATA, "beancounter", None, color, scale),
    "TTR Ambulance Chaser": MAKECOG( departmentLaw, TTR_COG_B_DATA, "ambulancechaser", None, color, scale),
    "TTR Micromanager": MAKECOG( departmentBoss, TTR_COG_C_DATA, "micromanager", None, color, scale),

    "TTR Mover & Shaker": MAKECOG( departmentSell, TTR_COG_B_DATA, "movershaker", None, color, scale),
    "TTR Number Cruncher": MAKECOG( departmentCash, TTR_COG_A_DATA, "numbercruncher", None, color, scale),
    "TTR Back Stabber": MAKECOG( departmentLaw, TTR_COG_A_DATA, "backstabber", None, color, scale),
    "TTR Downsizer": MAKECOG( departmentBoss, TTR_COG_B_DATA, "beancounter", None, color, scale),

    "TTR Two-Face": MAKECOG( departmentSell, TTR_COG_A_DATA, "twoface", None, color, scale),
    "TTR Money Bags": MAKECOG( departmentCash, TTR_COG_C_DATA, "moneybags", None, color, scale),
    "TTR Spin Doctor": MAKECOG( departmentLaw, TTR_COG_B_DATA, "telemarketer", "**/spin-doctor", color, scale),
    "TTR Head Hunter": MAKECOG( departmentBoss, TTR_COG_A_DATA, "headhunter", None, color, scale),

    "TTR The Mingler": MAKECOG( departmentSell, TTR_COG_A_DATA, "twoface", "**/mingler", color, scale),
    "TTR Loan Shark": MAKECOG( departmentCash, TTR_COG_B_DATA, "loanshark", None, color, scale),
    "TTR Legal Eagle": MAKECOG( departmentLaw, TTR_COG_A_DATA, "legaleagle", None, color, scale),
    "TTR Corporate Raider": MAKECOG( departmentBoss, TTR_COG_C_DATA, "tightwad", "**/corporate-raider", color, scale),

    "TTR Mr. Hollywood": MAKECOG( departmentSell, TTR_COG_A_DATA, "yesman", None, color, scale),
    "TTR Robber Baron": MAKECOG( departmentCash, TTR_COG_A_DATA, "yesman", "**/robber-baron", color, scale),
    "TTR Big Wig": MAKECOG( departmentLaw, TTR_COG_A_DATA, "bigwig", None, color, scale),
    "TTR The Big Cheese": MAKECOG( departmentBoss, TTR_COG_A_DATA, "bigcheese", None, color, scale),
}


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
