from pyfrotz.ovos import FrotzSkill


class Zork3Skill(FrotzSkill):
    def __init__(self, *args, **kwargs):
        # TODO - dedicated icon, use pyfrotz icon for now
        skill_icon = "https://raw.githubusercontent.com/TigreGotico/pyFrotz/refs/heads/dev/pyfrotz/gui/all/pyfrotz.png"
        bg = "http://infocom.elsewhere.org/gallery/zork3/front.jpg"
        # game is english only, apply bidirectional translation
        super().__init__(*args,
                         game_id="zork_3",
                         game_lang="en-us",
                         game_data=f'{self.root_dir}/res/{self.game_id}.z5',
                         skill_icon=skill_icon,
                         game_image=bg,
                         **kwargs)
