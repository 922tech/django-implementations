const path = require("path");
const webpack = require("webpack");
// var ManifestPlugin = require("webpack-manifest-plugin");





module.exports = {
  experiments: {
    topLevelAwait: true
  },
  entry: "./src/index.js",
  output: {
    path: path.resolve(__dirname, "./static/frontend"),
    filename: "[name].js",
  },
  module: {
    rules: [
      {
        test: /\.js|.jsx$/,
        exclude: /node_modules/,
        use: "babel-loader",
      },
      {
        test: /\.css$/,
        exclude: /node_modules/,
        use: ["style-loader", "css-loader"],
      },
    ],
  },
  optimization: {
    minimize: true,
  },
  plugins: [
    new webpack.DefinePlugin({
      "process.env": {
        NODE_ENV: JSON.stringify("development"),
      },


    }),
  ],
  resolve: {
    extensions: ['', '.js', '.jsx'],
  }
};

