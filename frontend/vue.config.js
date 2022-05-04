// vue.config.js

module.exports = {
  publicPath: '/',
  configureWebpack: {
    performance: {
      hints: 'warning',
      maxAssetSize: 2048576,
      maxEntrypointSize: 2048576
    }
  },
  devServer: {
    // proxy: {
    //   '^/js': {
    //     target: 'http://localhost:80/'
    //   },
    //   '^/img': {
    //     target: 'http://localhost:80/'
    //   },
    //   '^/static': {
    //     target: 'http://localhost:80/'
    //   }
    // },
    allowedHosts: 'all',
    https: false,
    host: "0.0.0.0",
    port: 80
  }
};
