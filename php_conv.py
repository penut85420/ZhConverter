import re
import pickle as pk

hant_pattern = re.compile(r'public static \$zh2Hant = \[([^]]*)]', re.M)
pair_pattern = re.compile(r'\'([^\']+)\' => \'([^\']+)\'')
hans_pattern = re.compile(r'public static \$zh2Hans = \[([^]]*)]', re.M)

def make_dict(data, pattern, file_path):
    with open(file_path, 'w', encoding='UTF-8') as fout:
        for p in pattern.findall(data):
            for pp in pair_pattern.findall(p):
                fout.write('%s\t%s\n' % pp)

def load_dict(file_path):
    conv = dict()
    conv['dict'] = dict()
    with open(file_path, 'r', encoding='UTF-8') as fin:
        for line in fin:
            line = line.strip().split('\t')
            n = len(line[0])
            dd = conv['dict'].get(n, dict())
            dd[line[0]] = line[1]
            conv['dict'][n] = dd
    conv['length'] = sorted(list(conv['dict'].keys()), reverse=True)
    return conv

if __name__ == '__main__':
    with open('./ZhConversion.php', 'r', encoding='UTF-8') as fin:
        data = fin.read()
        make_dict(data, hant_pattern, './zhhans2t.txt')
        make_dict(data, hans_pattern, './zhhant2s.txt')

    with open('./zhhans2t.pkl', 'wb') as pkl:
        pk.dump(load_dict('./zhhans2t.txt'), pkl)

    with open('./zhhant2s.pkl', 'wb') as pkl:
        pk.dump(load_dict('./zhhant2s.txt'), pkl)