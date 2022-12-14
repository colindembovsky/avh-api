"use strict";

Object.defineProperty(exports, "__esModule", {
  value: true
});
exports["default"] = void 0;
var _ApiClient = _interopRequireDefault(require("../ApiClient"));
function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { "default": obj }; }
function _typeof(obj) { "@babel/helpers - typeof"; return _typeof = "function" == typeof Symbol && "symbol" == typeof Symbol.iterator ? function (obj) { return typeof obj; } : function (obj) { return obj && "function" == typeof Symbol && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }, _typeof(obj); }
function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
function _defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, _toPropertyKey(descriptor.key), descriptor); } }
function _createClass(Constructor, protoProps, staticProps) { if (protoProps) _defineProperties(Constructor.prototype, protoProps); if (staticProps) _defineProperties(Constructor, staticProps); Object.defineProperty(Constructor, "prototype", { writable: false }); return Constructor; }
function _toPropertyKey(arg) { var key = _toPrimitive(arg, "string"); return _typeof(key) === "symbol" ? key : String(key); }
function _toPrimitive(input, hint) { if (_typeof(input) !== "object" || input === null) return input; var prim = input[Symbol.toPrimitive]; if (prim !== undefined) { var res = prim.call(input, hint || "default"); if (_typeof(res) !== "object") return res; throw new TypeError("@@toPrimitive must return a primitive value."); } return (hint === "string" ? String : Number)(input); }
/**
 * The KernelThread model module.
 * @module model/KernelThread
 * @version 1.0.2
 */
var KernelThread = /*#__PURE__*/function () {
  /**
   * Constructs a new <code>KernelThread</code>.
   * 
   * @alias module:model/KernelThread
   */
  function KernelThread() {
    _classCallCheck(this, KernelThread);
    KernelThread.initialize(this);
  }

  /**
   * Initializes the fields of this object.
   * This method is used by the constructors of any subclasses, in order to implement multiple inheritance (mix-ins).
   * Only for internal use.
   */
  _createClass(KernelThread, null, [{
    key: "initialize",
    value: function initialize(obj) {}

    /**
     * Constructs a <code>KernelThread</code> from a plain JavaScript object, optionally creating a new instance.
     * Copies all relevant properties from <code>data</code> to <code>obj</code> if supplied or a new instance if not.
     * @param {Object} data The plain JavaScript object bearing properties of interest.
     * @param {module:model/KernelThread} obj Optional instance to populate.
     * @return {module:model/KernelThread} The populated <code>KernelThread</code> instance.
     */
  }, {
    key: "constructFromObject",
    value: function constructFromObject(data, obj) {
      if (data) {
        obj = obj || new KernelThread();
        if (data.hasOwnProperty('kernelId')) {
          obj['kernelId'] = _ApiClient["default"].convertToType(data['kernelId'], 'String');
        }
        if (data.hasOwnProperty('tid')) {
          obj['tid'] = _ApiClient["default"].convertToType(data['tid'], 'Number');
        }
        if (data.hasOwnProperty('stack')) {
          obj['stack'] = _ApiClient["default"].convertToType(data['stack'], ['String']);
        }
      }
      return obj;
    }
  }]);
  return KernelThread;
}();
/**
 * Kernel Thread ID
 * @member {String} kernelId
 */
KernelThread.prototype['kernelId'] = undefined;

/**
 * Task ID
 * @member {Number} tid
 */
KernelThread.prototype['tid'] = undefined;

/**
 * Array of stack addresses
 * @member {Array.<String>} stack
 */
KernelThread.prototype['stack'] = undefined;
var _default = KernelThread;
exports["default"] = _default;