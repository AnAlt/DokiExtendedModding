image protag 1a = im.Composite((960, 960), (0, 40), "mod_assets/MC/1a.png")
image protag 1b = im.Composite((960, 960), (0, 40), "mod_assets/MC/1b.png")
image protag 1c = im.Composite((960, 960), (0, 40), "mod_assets/MC/1c.png")
image protag 1d = im.Composite((960, 960), (0, 40), "mod_assets/MC/1d.png")
image protag 1e = im.Composite((960, 960), (0, 40), "mod_assets/MC/1e.png")
image protagdizzy = im.Composite((960, 960), (0, 40), "mod_assets/MC/1e.png")
image protag 1f = im.Composite((960, 960), (0, 40), "mod_assets/MC/1f.png")
image protag 1g = im.Composite((960, 960), (0, 40), "mod_assets/MC/1g.png")
image mc_dizzy:
    contains:
        im.Composite((960, 960), (0, 40), "mod_assets/MC/1e.png")
        zoom 1.0 xalign 0.5 yalign 0.05
    parallel:
        dizzy(1, 1.0)
    parallel:
        alpha 0.3
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.3
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.4
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.5
        linear 0.25 alpha 0.6
        linear 0.25 alpha 0.4
        repeat
