DIR="/Users/pratapsingh/Desktop/Personal/Learning/schoolPat_Prod-"`date +"%Y-%m-%d"`""
if [ -d "$DIR" ]; then
  ### Take action if $DIR exists ###
  echo "Installing config files in ${DIR}..."
else
  ###  Control will jump here if $DIR does NOT exists ###
  echo "Error: ${DIR} not found. Can not continue."
  exit 1
fi
