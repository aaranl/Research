import numpy as np

def create_letter_patterns():
    patterns = {}

    patterns['A'] = np.full(shape=(8, 8), fill_value=1)
    patterns['A'][0][0:8] = 0
    patterns['A'][1][0:8] = 0
    patterns['A'][2][0:2] = patterns['A'][2][6:8] = 0
    patterns['A'][3][0:2] = patterns['A'][3][6:8] = 0
    patterns['A'][4][0:8] = 0
    patterns['A'][5][0:2] = patterns['A'][5][6:8] = 0
    patterns['A'][6][0:2] = patterns['A'][6][6:8] = 0
    patterns['A'][7][0:2] = patterns['A'][7][6:8] = 0

    patterns['B'] = np.full(shape=(8, 8), fill_value=1)
    patterns['B'][1][0:8] = 0
    patterns['B'][2][0:2] = patterns['B'][2][6:8] = 0
    patterns['B'][3][0:2] = patterns['B'][3][6:8] = 0
    patterns['B'][4][0:8] = 0
    patterns['B'][5][0:2] = patterns['B'][5][6:8] = 0
    patterns['B'][6][0:2] = patterns['B'][6][6:8] = 0
    patterns['B'][7][0:8] = 0

    patterns['C'] = np.full(shape=(8, 8), fill_value=1)
    patterns['C'][0][0:7] = 0
    patterns['C'][1][0:2] = 0
    patterns['C'][2][0:2] = 0
    patterns['C'][3][0:2] = 0
    patterns['C'][4][0:2] = 0
    patterns['C'][5][0:2] = 0
    patterns['C'][6][0:2] = 0
    patterns['C'][7][0:7] = 0

    patterns['D'] = np.full(shape=(8, 8), fill_value=1)
    patterns['D'][0][0:5] = 0
    patterns['D'][1][0:1] = patterns['D'][1][5:6] = 0
    patterns['D'][2][0:1] = patterns['D'][2][5:6] = 0
    patterns['D'][3][0:1] = patterns['D'][3][5:6] = 0
    patterns['D'][4][0:1] = patterns['D'][4][5:6] = 0
    patterns['D'][5][0:1] = patterns['D'][5][5:6] = 0
    patterns['D'][6][0:1] = patterns['D'][6][5:6] = 0
    patterns['D'][7][0:5] = 0

    patterns['E'] = np.full(shape=(8, 8), fill_value=1)
    patterns['E'][0][0:7] = 0
    patterns['E'][1][0:2] = 0
    patterns['E'][2][0:2] = 0
    patterns['E'][3][0:7] = 0
    patterns['E'][4][0:2] = 0
    patterns['E'][5][0:2] = 0
    patterns['E'][6][0:7] = 0

    patterns['F'] = np.full(shape=(8, 8), fill_value=1)
    patterns['F'][0][0:7] = 0
    patterns['F'][1][0:2] = 0
    patterns['F'][2][0:2] = 0
    patterns['F'][3][0:2] = 0
    patterns['F'][4][0:7] = 0
    patterns['F'][5][0:2] = 0
    patterns['F'][6][0:2] = 0
    patterns['F'][7][0:2] = 0

    # patterns['G'] = np.full(shape=(8, 8), fill_value=1)
    # patterns['G'][0][0:7] = 0
    # patterns['G'][1][0:1] = 0
    # patterns['G'][2][0:1] = 0
    # patterns['G'][3][0:1] = 0
    # patterns['G'][4][0:1] = 0
    # patterns['G'][5][0:1] = patterns['G'][5][3:7] = 0
    # patterns['G'][6][0:1] = patterns['G'][6][3:4] = patterns['G'][6][6:7] = 0
    # patterns['G'][7][0:4] = patterns['G'][7][6:7] = 0

    patterns['H'] = np.full(shape=(8, 8), fill_value=1)
    patterns['H'][0][0:2] = patterns['H'][0][6:8] = 0
    patterns['H'][1][0:2] = patterns['H'][1][6:8] = 0
    patterns['H'][2][0:2] = patterns['H'][2][6:8] = 0
    patterns['H'][3][0:8] = 0
    patterns['H'][4][0:8] = 0
    patterns['H'][5][0:2] = patterns['H'][5][6:8] = 0
    patterns['H'][6][0:2] = patterns['H'][6][6:8] = 0
    patterns['H'][7][0:2] = patterns['H'][7][6:8] = 0

    patterns['I'] = np.full(shape=(8, 8), fill_value=1)
    patterns['I'][0][0:8] = 0
    patterns['I'][1][0:8] = 0
    patterns['I'][2][3:5] = 0
    patterns['I'][3][3:5] = 0
    patterns['I'][4][3:5] = 0
    patterns['I'][5][3:5] = 0
    patterns['I'][6][0:8] = 0
    patterns['I'][7][0:8] = 0

    patterns['J'] = np.full(shape=(8, 8), fill_value=1)
    patterns['J'][0][1:8] = 0
    patterns['J'][1][4:5] = 0
    patterns['J'][2][4:5] = 0
    patterns['J'][3][4:5] = 0
    patterns['J'][4][4:5] = 0
    patterns['J'][5][1:2] = patterns['J'][5][4:5] = 0
    patterns['J'][6][1:2] = patterns['J'][6][4:5] = 0
    patterns['J'][7][1:5] = 0

    patterns['K'] = np.full(shape=(8, 8), fill_value=1)
    patterns['K'][0][0:2] = patterns['K'][0][5:6] = 0
    patterns['K'][1][0:2] = patterns['K'][1][4:5] = 0
    patterns['K'][2][0:2] = patterns['K'][2][3:4] = 0
    patterns['K'][3][0:3] = 0
    patterns['K'][4][0:3] = 0
    patterns['K'][5][0:2] = patterns['K'][5][3:4] = 0
    patterns['K'][6][0:2] = patterns['K'][6][4:5] = 0
    patterns['K'][7][0:2] = patterns['K'][7][5:6] = 0

    patterns['L'] = np.full(shape=(8, 8), fill_value=1)
    patterns['L'][0][0:2] = 0
    patterns['L'][1][0:2] = 0
    patterns['L'][2][0:2] = 0
    patterns['L'][3][0:2] = 0
    patterns['L'][4][0:2] = 0
    patterns['L'][5][0:2] = 0
    patterns['L'][6][0:8] = 0
    patterns['L'][7][0:8] = 0

    patterns['M'] = np.full(shape=(8, 8), fill_value=1)
    patterns['M'][0][0:2] = patterns['M'][0][6:8] = 0
    patterns['M'][1][0:3] = patterns['M'][1][5:8] = 0
    patterns['M'][2][0:2] = patterns['M'][2][3:5] = patterns['M'][2][6:8] = 0
    patterns['M'][3][0:2] = patterns['M'][3][6:8] = 0
    patterns['M'][4][0:2] = patterns['M'][4][6:8] = 0
    patterns['M'][5][0:2] = patterns['M'][5][6:8] = 0
    patterns['M'][6][0:2] = patterns['M'][6][6:8] = 0
    patterns['M'][7][0:2] = patterns['M'][7][6:8] = 0

    patterns['N'] = np.full(shape=(8, 8), fill_value=1)
    patterns['N'][1][0:2] = patterns['N'][1][7:8] = 0
    patterns['N'][2][0:1] = patterns['N'][2][2:3] = patterns['N'][2][7:8] = 0
    patterns['N'][3][0:1] = patterns['N'][3][3:4] = patterns['N'][3][7:8] = 0
    patterns['N'][4][0:1] = patterns['N'][4][4:5] = patterns['N'][4][7:8] = 0
    patterns['N'][5][0:1] = patterns['N'][5][5:6] = patterns['N'][5][7:8] = 0
    patterns['N'][6][0:1] = patterns['N'][6][6:8] = 0

    patterns['O'] = np.full(shape=(8, 8), fill_value=1)
    patterns['O'][0][2:6] = 0
    patterns['O'][1][1:2] = patterns['O'][1][6:7] = 0
    patterns['O'][2][1:2] = patterns['O'][2][6:7] = 0
    patterns['O'][3][1:2] = patterns['O'][3][6:7] = 0
    patterns['O'][4][1:2] = patterns['O'][4][6:7] = 0
    patterns['O'][5][1:2] = patterns['O'][5][6:7] = 0
    patterns['O'][6][1:2] = patterns['O'][6][6:7] = 0
    patterns['O'][7][2:6] = 0

    patterns['P'] = np.full(shape=(8, 8), fill_value=1)
    patterns['P'][0][0:6] = 0
    patterns['P'][1][0:2] = patterns['P'][1][5:6] = 0
    patterns['P'][2][0:2] = patterns['P'][2][5:6] = 0
    patterns['P'][3][0:2] = patterns['P'][3][5:6] = 0
    patterns['P'][4][0:6] = 0
    patterns['P'][5][0:2] = 0
    patterns['P'][6][0:2] = 0
    patterns['P'][7][0:2] = 0

    patterns['Q'] = np.full(shape=(8, 8), fill_value=1)
    patterns['Q'][0][2:6] = 0
    patterns['Q'][1][1:2] = patterns['Q'][1][6:7] = 0
    patterns['Q'][2][1:2] = patterns['Q'][2][6:7] = 0
    patterns['Q'][3][1:2] = patterns['Q'][3][6:7] = 0
    patterns['Q'][4][1:2] = patterns['Q'][4][4:5] = patterns['Q'][4][6:7] = 0
    patterns['Q'][5][1:2] = patterns['Q'][5][5:6] = patterns['Q'][5][6:7] = 0
    patterns['Q'][6][2:7] = 0
    patterns['Q'][7][7:8] = 0

    patterns['R'] = np.full(shape=(8, 8), fill_value=1)
    patterns['R'][0][0:6] = 0
    patterns['R'][1][0:2] = patterns['R'][1][5:6] = 0
    patterns['R'][2][0:2] = patterns['R'][2][5:6] = 0
    patterns['R'][3][0:6] = 0
    patterns['R'][4][0:2] = patterns['R'][4][2:3] = 0
    patterns['R'][5][0:2] = patterns['R'][5][3:4] = 0
    patterns['R'][6][0:2] = patterns['R'][6][4:5] = 0
    patterns['R'][7][0:2] = patterns['R'][7][5:6] = 0

    patterns['S'] = np.full(shape=(8, 8), fill_value=1)
    patterns['S'][0][0:8] = 0
    patterns['S'][1][0:1] = 0
    patterns['S'][2][0:1] = 0
    patterns['S'][3][0:8] = 0
    patterns['S'][4][7:8] = 0
    patterns['S'][5][7:8] = 0
    patterns['S'][6][0:8] = 0

    patterns['T'] = np.full(shape=(8, 8), fill_value=1)
    patterns['T'][0][0:8] = 0
    patterns['T'][1][0:8] = 0
    patterns['T'][2][3:5] = 0
    patterns['T'][3][3:5] = 0
    patterns['T'][4][3:5] = 0
    patterns['T'][5][3:5] = 0
    patterns['T'][6][3:5] = 0
    patterns['T'][7][3:5] = 0

    patterns['U'] = np.full(shape=(8, 8), fill_value=1)
    patterns['U'][0][0:2] = patterns['U'][0][6:8] = 0
    patterns['U'][1][0:2] = patterns['U'][1][6:8] = 0
    patterns['U'][2][0:2] = patterns['U'][2][6:8] = 0
    patterns['U'][3][0:2] = patterns['U'][3][6:8] = 0
    patterns['U'][4][0:2] = patterns['U'][4][6:8] = 0
    patterns['U'][5][0:2] = patterns['U'][5][6:8] = 0
    patterns['U'][6][0:2] = patterns['U'][6][6:8] = 0
    patterns['U'][7][1:7] = 0

    patterns['V'] = np.full(shape=(8, 8), fill_value=1)
    patterns['V'][0][0:2] = patterns['V'][0][6:8] = 0
    patterns['V'][1][0:2] = patterns['V'][1][6:8] = 0
    patterns['V'][2][0:2] = patterns['V'][2][6:8] = 0
    patterns['V'][3][0:2] = patterns['V'][3][6:8] = 0
    patterns['V'][4][1:3] = patterns['V'][4][5:7] = 0
    patterns['V'][5][1:3] = patterns['V'][5][5:7] = 0
    patterns['V'][6][2:4] = patterns['V'][6][4:6] = 0
    patterns['V'][7][3:5] = 0

    # patterns['W'] = np.full(shape=(8, 8), fill_value=1)
    # patterns['W'][0][0:2] = patterns['W'][0][6:8] = 0
    # patterns['W'][1][0:2] = patterns['W'][1][6:8] = 0
    # patterns['W'][2][0:2] = patterns['W'][2][6:8] = 0
    # patterns['W'][3][0:2] = patterns['W'][3][6:8] = 0
    # patterns['W'][4][0:2] = patterns['W'][4][6:8] = 0
    # patterns['W'][5][0:2] = patterns['W'][5][6:8] = 0
    # patterns['W'][6][1:3] = patterns['W'][6][5:7] = 0
    # patterns['W'][7][2:6] = 0

    patterns['X'] = np.full(shape=(8, 8), fill_value=1)
    patterns['X'][0][0:2] = patterns['X'][0][6:8] = 0
    patterns['X'][1][1:3] = patterns['X'][1][5:7] = 0
    patterns['X'][2][2:4] = patterns['X'][2][4:6] = 0
    patterns['X'][3][3:5] = 0
    patterns['X'][4][3:5] = 0
    patterns['X'][5][2:4] = patterns['X'][5][4:6] = 0
    patterns['X'][6][1:3] = patterns['X'][6][5:7] = 0
    patterns['X'][7][0:2] = patterns['X'][7][6:8] = 0

    patterns['Y'] = np.full(shape=(8, 8), fill_value=1)
    patterns['Y'][0][0:2] = patterns['Y'][0][6:8] = 0
    patterns['Y'][1][1:3] = patterns['Y'][1][5:7] = 0
    patterns['Y'][2][2:4] = patterns['Y'][2][4:6] = 0
    patterns['Y'][3][3:5] = 0
    patterns['Y'][4][3:5] = 0
    patterns['Y'][5][3:5] = 0
    patterns['Y'][6][3:5] = 0
    patterns['Y'][7][3:5] = 0

    patterns['Z'] = np.full(shape=(8, 8), fill_value=1)
    patterns['Z'][0][0:8] = 0
    patterns['Z'][1][6:8] = 0
    patterns['Z'][2][5:7] = 0
    patterns['Z'][3][4:6] = 0
    patterns['Z'][4][3:5] = 0
    patterns['Z'][5][2:4] = 0
    patterns['Z'][6][1:3] = 0
    patterns['Z'][7][0:8] = 0

    return patterns


