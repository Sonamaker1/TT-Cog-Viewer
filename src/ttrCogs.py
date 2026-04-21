def os_path_join(*in_args):
    return "/".join(in_args)
    

RESOURCES_DIR = "resources"


# ***************** COG SUIT TEXTURES ***************
TTR_SELLBOT_SUIT = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "s_blazer.jpg")

TTR_CASHBOT_SUIT = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "m_blazer.jpg")

TTR_LAWBOT_SUIT = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "l_blazer.jpg")

TTR_BOSSBOT_SUIT = os_path_join(RESOURCES_DIR, "phase_3.5", "maps", "c_blazer.jpg")

TTR_WAITER_SUIT = os_path_join(RESOURCES_DIR, "phase_12", "maps", "ttcc_ene_suittex_waiter.png")

TTR_SUIT_MODEL_C_HEADS = os_path_join(RESOURCES_DIR, "phase_3.5", "models", "char", "ttr_r_ene_cgc_heads.bam")


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

TTR_COG_DATA = {
    # *******************   SELLBOTS **********************************
    "TTR Bottom Feeder": {"suitTex": TTR_SELLBOT_SUIT,
                "head": TTR_SUIT_MODEL_C_HEADS,
                "hands": (191 / 255, 191 / 255, 242 / 255, 1),
                "name": "ttr_r_ene_cgc_heads",
                "scale": 0.96618,
                "dept": "l",
                "cog": "tightwad",
                "headTextureName": "**/bottom-feeder",
                "headTextureModel": "resources/phase_3.5/models/char/ttr_m_ene_cgc_heads_textures.bam",
                "suit": "ttrc",
                "suitToggle": "y",
                "emblem": "emblem_legal"
    },
}
