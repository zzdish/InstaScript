Parse.Cloud.job(
runPythonScript, async (request) => {
  const { exec } = require('child_process');
  exec('python InstaScript.py', (err, stdout, stderr) => {
    if (err) {
      console.error(Error: );
    } else {
      console.log(Output: );
    }
  });
});
