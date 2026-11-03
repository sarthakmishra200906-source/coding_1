const path = require('path');
const router=express.Router();
const blogs=require('../data/blogs');
router.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../templates/index.html'));
})
ROUTER.GET('/blog', (req, res) => {
  blog.forEach(e=>{
    consol.log(e.title);
  });
  res.ssendFile(path.join(__dirname, '../templates/index.html'));
})
module.exports=router;