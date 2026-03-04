#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import json
import random
import logging


def setup_logging(level):
    logging.basicConfig(
        level=level,      
        format="%(asctime)s [%(levelname)s] %(message)s",
    )

def load_character(name):
    if not hasattr(load_character, "_cache"):
        load_character._cache = {}
    if name in load_character._cache:
        return load_character._cache[name]
    try:
        with open(f"{name}.json") as f:
            data =  json.load(f)
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Character file {name}.json not found") from e
    except json.JSONDecodeError as e:
        raise ValueError(f" {name}.json invalid") from e
    
    load_character._cache[name] = data
    return data


def load_skills():
    if not hasattr(load_skills, "_cache"):
        try:
            with open("skill_list.json") as f:
                load_skills._cache = json.load(f)
        except FileNotFoundError as e:
            raise FileNotFoundError(f"Skill file .skill_list.json not found") from e
        except json.JSONDecodeError as e:
            raise ValueError(f"skill file is invalid") from e
    return load_skills._cache


def roll_dice():
    rolls = [random.randint(1,20) for roll in range(3)]
    return rolls

def success_rate(attributes, points):
    total = 8000.0 # 20**3
    success = 0
    for d1 in range(1,21):
        for d2 in range(1,21):
            for d3 in range(1,21):
                rolls = [d1, d2, d3]
                if rolls.count(1)>=2:
                    success += 1
                    continue
                
                if rolls.count(20)>=2:
                    continue

                diff = [max(0, roll - attribute) for roll, attribute in zip(rolls, attributes)]
                if sum(diff) <= points:
                    success += 1
    logging.info(f"{points}")
    logging.info(f"{success}")
    return success/total*100

def get_values(character, skill_list, skill):
    try:
        skillpoints = int(character["Skillpoints"][skill])
        skill_parts = skill_list[skill]
    except KeyError as e:                           
        raise KeyError(f"Skill not found: {e}") from e
    except ValueError as e:
        raise ValueError(f"Skill points must be integers") from e
    except TypeError as e:
        raise TypeError(f"Skill has invalid Type") from e
    
    try:
        values = [int(character["Attributes"][attr]) for attr in skill_parts]
    except KeyError as e:                           
        raise KeyError(f"Attribut not found: {e}") from e
    except ValueError as e:
        raise ValueError(f"Attributes must be integers") from e
    except TypeError as e:
        raise TypeError(f"Attributes has invalid Type") from e
    return values, skillpoints

def resolve_roll(attribute_values, rolls, skill_points):
    logging.info(f"attribute_values={attribute_values}, rolls={rolls}, points={skill_points}")

    #any value 0 or under, roll not permitted
    if any(value<=0 for value in attribute_values):
        return "Eigenschaft 0 oder negativ. Probe nicht erlaubt"
    
    compare = [value-roll for value, roll in zip(attribute_values, rolls)]
    logging.debug(f"Über: {compare}")

    roll_success = all(x>=0 for x in compare)
    logging.debug(f"Erfolgreich: {roll_success}")

    remainder = None

    if rolls.count(1) >=2:
        return f"Kritischer Erfolg"
    elif rolls.count(20) >= 2:
        return f"Patzer"
    elif roll_success:
        return f"Sauber Gelungen Quali: {int((3+skill_points-1)/3)}"
    else:
        difference = [fail for fail in compare if fail < 0]
        remainder = skill_points + sum(difference)
        logging.debug(f"Punkte über: {sum(difference)}, {skill_points}")
        logging.info(f"Rest: {remainder}")

    if remainder <= 2 and remainder >= 0:
        return f"Gelungen Quali: 1 {remainder}"       
    elif remainder > 0:
        return f"Gelungen Quali: {int((3+remainder-1)/3)} {remainder}"
    else:
        return "Gescheitert"


def skill_check(character, skill_list, skill):
    values, skillpoints = get_values(character,  skill_list, skill)
    probability = success_rate(values, skillpoints)
    logging.info(f"Erfolgswahrscheinlichkeit: {probability}")
    rolls = roll_dice()
    return resolve_roll(values, rolls,  skillpoints)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--log-level", default="DEBUG")
    parser.add_argument("--char", default="alrik")
    parser.add_argument("--skill", default="Riding")
    args = parser.parse_args()

    setup_logging(args.log_level.upper())
    logger = logging.getLogger(__name__)


    char_name = args.char 
    skill_name = args.skill

    logging.info(f"Nutze Charakter '{char_name}' und Skill '{skill_name}'")

    character = load_character(char_name)
    skills = load_skills()
    result = skill_check(character, skills, skill_name)
    print(result)


if __name__ == "__main__":
    main()