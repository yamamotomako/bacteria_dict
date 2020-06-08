#! /usr/bin/env python

import os,sys

dupli_dict = []
dupli_dict_strain = []

strain_file = open("./strain.tsv", "w")
strain_file.write("\t".join(["phylum","class","order","family","genus","species","strain"])+"\n")

species_file = open("./species.tsv", "w")
species_file.write("\t".join(["phylum","class","order","family","genus","species"])+"\n")

with open("./all2.tsv", "r") as f:
    lines = f.read().split("\n")
    for line in lines:
        if line[:6] == "phylum":
            continue
        if line == "":
            continue

        data = line.split("\t")
        phylum = data[0]
        class_ = data[1]
        order = data[2]
        family = data[3]
        genus = data[4]
        species = data[5]
        strain = data[6]

        concate = phylum+class_+order+family+genus+species
        concate2 = phylum+class_+order+family+genus+species+strain
        #print strain

        if phylum.find("assigned") != -1:
            phylum = ""
        if class_.find("assigned") != -1:
            class_ = ""
        if order.find("assigned") != -1:
            order = ""
        if family.find("assigned") != -1:
            family = ""
        if genus.find("assigned") != -1:
            genus = ""
        if species.find("assigned") != -1:
            species = ""
        if strain.find("assigned") != -1:
            strain = ""


        if not species in dupli_dict and order != "":
            dupli_dict.append(species)
            species_file.write("\t".join([phylum,class_,order,family,genus,species])+"\n")

        if not concate2 in dupli_dict_strain:
            dupli_dict_strain.append(concate2)
            strain_file.write("\t".join([phylum,class_,order,family,genus,species,strain])+"\n")

species_file.close()
strain_file.close()

