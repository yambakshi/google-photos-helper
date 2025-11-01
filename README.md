# Google Photos Helper
Google Photos helper for actions that are not possible from the UI

## Technologies
- Python 3.14.0

## Setup
### 1. Virtual Environment
Open `VSCode` from the repo's root, open the terminal, and create a virtual environment named `env`:
```
py -m venv env
```

**Windows 10**
1. Check the current execution policy (in order to activate the virtual environment in `VSCode`'s terminal you'll first need to enable running powershell scripts):
   ```
   get-executionpolicy
   ```
2. The default execution policy, `Restricted`, is preventing you from running the virtual environment's activation script that's in:
   ```
   env\Scripts\Activate
   ```
3. Set the execution policy for the current user to `RemoteSigned`:
   ```
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
4. Activate the virtual environment:
   ```
   env\Scripts\Activate
   ```

**Mac**
1. Activate the virtual environment:
   ```
   source env/bin/activate
   ```

**Usefull Commands**
- Deactivate the virtual environment:
   ```
   deactivate
   ```

### 2. PIP Packages
1. Before installing the `pip` packages, make sure that the `env` virtual environment is activated (notice the `(env)` in the beginning):
   ```
   (env) PS D:\Yam Bakshi\Careers\Hi-Tech\Portfolio\Python\Google Photos Helper >
   ```

2. Install `pip` packages:
   ```
   py -m pip install -r requirements.txt
   ```

**Windows 10**
- `pip` packages folders:
   - Virtual Environment - `<repo_root>\env\Lib\site-packages`
   - Global - `C:\users\yamba\AppData...` // FIX THIS

**Useful Commands**
- Updating `requirements.txt` with currently installed `pip` packages (-l or --local flag to save only local packages and not global):
   ```
   pip freeze -l > requirements.txt
   ```

### 3. Google API Authentication
The `Google API` authentication is done with the `./authentication/credentials.json` file.

The first time you authenticate, a `token.pickle` file will be generated and saved in the `./authentication` folder.

The `token.pickle` will expire after some time, so you'll have to delete it manually in order for a new one to be generated:
```
rm -rf ./authentication/token.pickle
```

### 4. VSCode Python Interpreter
Set the virtual environment's interperter in `VSCode`:
1. Hit `Ctrl`+`Shift`+`P`.
2. Type `Python: Select Interpreter` and hit `Enter` to edit the setting.
3. Select `Python 3.14.0 ('env':venv) .\env\Scripts\python.exe`. // FIX THIS