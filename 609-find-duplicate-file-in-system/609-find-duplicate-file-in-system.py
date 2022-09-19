class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        mem = defaultdict(list)
        for i in paths:
            files = i.split(" ")
            path = files[0]
            for j in files[1:]:
                file_name, content = j.split("(")
                mem[content[:-1]].append(f"{path}/{file_name}")
        output = []
        for j in  mem.values():
            if len(j) > 1:
                output.append(j)
        return output
        