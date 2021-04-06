def get_len_of_str(s):
    # 아래 코드를 작성해주세요.
    str = ''
    arr = []
    for i in range(len(s)):
      if s[i] not in str:
        str += s[i]
      else:
        arr.append(str)
        str =''
        str += s[i]
    arr.append(str)
    return max(len(m) for m in arr)
print(get_len_of_str('abc decabfghij'))
