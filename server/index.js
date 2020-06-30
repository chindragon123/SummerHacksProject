const Koa = require('koa');
const koaLogger = require('koa-logger');
const Router = require('koa-router');

const app = new Koa();
const router = new Router();

app.use(koaLogger());

// Router middleware.
app.use(router.routes());
app.use(router.allowedMethods());

router.get('/', (ctx) => {
  ctx.body = "<h1>Poggurs<h1>";
});

app.listen(5000, () => {
  console.log('server on port 5000');
});
