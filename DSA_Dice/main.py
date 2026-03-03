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
    if name not in load_character._cache:
        with open(f"{name}.json") as f:
            load_character._cache[name] =  json.load(f)
    return load_character._cache[name]


def load_skills():
    if not hasattr(load_skills, "_cache"):
        with open("skill_list.json") as f:
            load_skills._cache = json.load(f)
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

def get_values(char, skills, skill):
    skillpoints = char["Skillpoints"][skill]
    skill_parts = skills[skill]                           
    
    values = [char["Attributes"][attr] for attr in skill_parts]
    return values, skillpoints

def resolve_roll(vals, rolls, points):
    logging.info(f"vals={vals}, rolls={rolls}, points={points}")

    #any value 0, roll not permitted
    if any(val==0 for val in vals):
        return "Eigenschaft 0. Probe nicht erlaubt"
    
    compare = [value-roll for value, roll in zip(vals, rolls)]
    logging.debug(f"Über: {compare}")

    roll_success = all(x>=0 for x in compare)
    logging.debug(f"Erfolgreich: {roll_success}")

    remainder = None

    if rolls.count(1) >=2:
        return f"Kritischer Erfolg"
    elif rolls.count(20) >= 2:
        return f"Patzer"
    elif roll_success:
        return f"Sauber Gelungen Quali: {int((3+points-1)/3)}"
    else:
        diff = [neg for neg in compare if neg < 0]
        remainder = points + sum(diff)
        logging.debug(f"Punkte über: {sum(diff)}, {points}")
        logging.info(f"Rest: {remainder}")

    if remainder <= 2 and remainder >= 0:
        return f"Gelungen Quali: 1 {remainder}"       
    elif remainder > 0:
        return f"Gelungen Quali: {int((3+remainder-1)/3)} {remainder}"
    else:
        return "fucked"


def skill_check(char, skills, skill):
    values, skillpoints = get_values(char, skills, skill)
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