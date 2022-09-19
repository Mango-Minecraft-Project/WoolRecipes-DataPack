from json import dump

def dump_(path, data):
    with open("./data/wool_tweaks/recipes/" + path + ".json", mode="w") as file:
        dump(data, file, indent=2)

dump_("wool_to_string", 
      {
          "type": "crafting_shapeless",
          "ingredients": [
              {
                  "tag": "wool_tweaks:wt_wool"
                  }
              ],
          "result": {
              "item":"minecraft:string", 
              "count":4
              }
          }
      )

for color in {"red", "black", "blue", "brown", 
              "cyan", "gray", "green", "light_blue", 
              "light_gray", "lime", "magenta", "orange", 
              "pink", "purple", "white", "yellow"}:
    # colored bed
    dump_(f"{color}_bed", 
          {
              "type": "crafting_shapeless",
              "group": "color_bed",
              "ingredients": [
                  {
                      "tag": "wool_tweaks:wt_bed"
                      },
                  {
                      "item": f"minecraft:{color}_dye"
                      }
                  ],
              "result": {
                  "item": f"minecraft:{color}_bed"
                  }
              }
          )
    
    # colored carpet
    dump_(f"{color}_carpet", 
          {
              "type": "crafting_shaped",
              "group":"color_carpet",
              "pattern": [
                  "***",
                  "*_*",
                  "***"
                  ],
              "key": 
                  {
                      "*": {
                          "tag": "wool_tweaks:wt_carpet"
                          },
                      "_": {
                          "item": f"minecraft:{color}_dye"
                          }
                      },
                  "result": {
                      "item": f"minecraft:{color}_carpet",
                      "count":9
                      }
                  }
          )
    
    # colored wool
    dump_(f"{color}_wool", 
          {
              "type": "crafting_shapeless",
              "group": "color_wool",
              "ingredients": [
                  {
                      "tag": "wool_tweaks:wt_wool"
                      },
                  {
                      "item": f"minecraft:{color}_dye"
                      }
                  ],
              "result": {
                  "item": f"minecraft:{color}_wool"
                  }
              }
          )