def count_face(face_line, face):
    count = 0
    while face_line:
        for c in left_face:
            if c in face_line:
                face_line.remove(c)
            else:
                return count
        count += 1


face_line = list(input())
left_face = list('(^^*)')
dummy_face_line = face_line.copy()
left_num = count_face(dummy_face_line, left_face)
right_face = list('(*^^)')
dummy_face_line = face_line.copy()
right_num = count_face(dummy_face_line, right_face)
print('{} {}'.format(left_num, right_num))
