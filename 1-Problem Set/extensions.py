def main():
  x = input("File name:\n").lower().strip()
  mime_type(x)

def mime_type(x):
  index = x.find(".")
  indexr = x.rfind(".")
  if index == indexr:
    extension = x[index+1:]
    match extension:
      case "gif" | "jpeg" | "png":
        print("image/" + extension)
      case "jpg":
        print("image/jpeg")
      case "pdf" | "zip":
        print("application/" + extension)
      case "txt":
        print("text/plain")
      case _:
        print("application/octet-stream")
  else:
    extension = x[indexr+1:]
    print("application/" + extension)

main()