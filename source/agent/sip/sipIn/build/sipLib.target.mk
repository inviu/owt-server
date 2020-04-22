# This file is generated by gyp; do not edit.

TOOLSET := target
TARGET := sipLib
### Rules for action "sipua_build":
quiet_cmd_binding_gyp_sipLib_target_sipua_build = ACTION binding_gyp_sipLib_target_sipua_build $@
cmd_binding_gyp_sipLib_target_sipua_build = LD_LIBRARY_PATH=$(builddir)/lib.host:$(builddir)/lib.target:$$LD_LIBRARY_PATH; export LD_LIBRARY_PATH; cd $(srcdir)/.; mkdir -p /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua; eval "cd /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua && make clean && make RE_HOME=$(CORE_HOME)/../../build/libdeps/build"

/root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/libsipua.a: obj := $(abs_obj)
/root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/libsipua.a: builddir := $(abs_builddir)
/root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/libsipua.a: TOOLSET := $(TOOLSET)
/root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/libsipua.a: /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/dtls_srtp/dtls_srtp.h /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/srtp/sdes.h /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/natpmp/libnatpmp.h /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/core.h /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/sipua_actions.h /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/vp8.h /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/include/sipua.h /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/include/baresip.h /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/dtls_srtp/dtls_srtp.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/dtls_srtp/dtls.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/dtls_srtp/srtp.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/turn/turn.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/srtp/sdes.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/srtp/srtp.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/natpmp/natpmp.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/natpmp/libnatpmp.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/ice/ice.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/zrtp/zrtp.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/modules/stun/stun.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/conf.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/mctrl.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/ua.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/aucodec.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/stream.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/bfcp.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/log.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/mock_sip_gateway.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/sipua_actions.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/vidcodec.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/metric.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/main.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/sipreq.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/audio.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/rtpkeep.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/mnat.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/menc.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/account.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/call.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/net.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/reg.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/uag.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/realtime.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/sipua.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/sdp.c /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/src/video.c FORCE_DO_CMD
	$(call do_cmd,binding_gyp_sipLib_target_sipua_build)

all_deps += /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/libsipua.a
action_binding_gyp_sipLib_target_sipua_build_outputs := /root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua/libsipua.a


DEFS_Debug := \
	'-DNODE_GYP_MODULE_NAME=sipLib' \
	'-DUSING_UV_SHARED=1' \
	'-DUSING_V8_SHARED=1' \
	'-DV8_DEPRECATION_WARNINGS=1' \
	'-D_LARGEFILE_SOURCE' \
	'-D_FILE_OFFSET_BITS=64' \
	'-DDEBUG' \
	'-D_DEBUG' \
	'-DV8_ENABLE_CHECKS'

# Flags passed to all source files.
CFLAGS_Debug := \
	-fPIC \
	-pthread \
	-Wall \
	-Wextra \
	-Wno-unused-parameter \
	-m64 \
	-g \
	-O0

# Flags passed to only C files.
CFLAGS_C_Debug :=

# Flags passed to only C++ files.
CFLAGS_CC_Debug := \
	-fno-rtti \
	-std=gnu++0x \
	-Wall \
	-O3 \
	-g \
	-std=c++0x

INCS_Debug := \
	-I/root/.cache/node-gyp/8.15.1/include/node \
	-I/root/.cache/node-gyp/8.15.1/src \
	-I/root/.cache/node-gyp/8.15.1/deps/openssl/config \
	-I/root/.cache/node-gyp/8.15.1/deps/openssl/openssl/include \
	-I/root/.cache/node-gyp/8.15.1/deps/uv/include \
	-I/root/.cache/node-gyp/8.15.1/deps/zlib \
	-I/root/.cache/node-gyp/8.15.1/deps/v8/include \
	-I$(srcdir)/sip_gateway \
	-I$(srcdir)/sip_gateway/sipua/include \
	-I$(CORE_HOME)/common \
	-I$(srcdir)/../../../../third_party/licode/erizo/src/erizo \
	-I$(CORE_HOME)/../../build/libdeps/build/include

DEFS_Release := \
	'-DNODE_GYP_MODULE_NAME=sipLib' \
	'-DUSING_UV_SHARED=1' \
	'-DUSING_V8_SHARED=1' \
	'-DV8_DEPRECATION_WARNINGS=1' \
	'-D_LARGEFILE_SOURCE' \
	'-D_FILE_OFFSET_BITS=64'

# Flags passed to all source files.
CFLAGS_Release := \
	-fPIC \
	-pthread \
	-Wall \
	-Wextra \
	-Wno-unused-parameter \
	-m64 \
	-O3 \
	-fno-omit-frame-pointer

# Flags passed to only C files.
CFLAGS_C_Release :=

# Flags passed to only C++ files.
CFLAGS_CC_Release := \
	-fno-rtti \
	-std=gnu++0x \
	-Wall \
	-O3 \
	-g \
	-std=c++0x

INCS_Release := \
	-I/root/.cache/node-gyp/8.15.1/include/node \
	-I/root/.cache/node-gyp/8.15.1/src \
	-I/root/.cache/node-gyp/8.15.1/deps/openssl/config \
	-I/root/.cache/node-gyp/8.15.1/deps/openssl/openssl/include \
	-I/root/.cache/node-gyp/8.15.1/deps/uv/include \
	-I/root/.cache/node-gyp/8.15.1/deps/zlib \
	-I/root/.cache/node-gyp/8.15.1/deps/v8/include \
	-I$(srcdir)/sip_gateway \
	-I$(srcdir)/sip_gateway/sipua/include \
	-I$(CORE_HOME)/common \
	-I$(srcdir)/../../../../third_party/licode/erizo/src/erizo \
	-I$(CORE_HOME)/../../build/libdeps/build/include

OBJS := \
	$(obj).target/$(TARGET)/sip_gateway/SipEP.o \
	$(obj).target/$(TARGET)/sip_gateway/SipGateway.o \
	$(obj).target/$(TARGET)/sip_gateway/SipCallConnection.o

# Add to the list of files we specially track dependencies for.
all_deps += $(OBJS)

# Make sure our actions/rules run before any of us.
$(OBJS): | $(action_binding_gyp_sipLib_target_sipua_build_outputs)

# CFLAGS et al overrides must be target-local.
# See "Target-specific Variable Values" in the GNU Make manual.
$(OBJS): TOOLSET := $(TOOLSET)
$(OBJS): GYP_CFLAGS := $(DEFS_$(BUILDTYPE)) $(INCS_$(BUILDTYPE))  $(CFLAGS_$(BUILDTYPE)) $(CFLAGS_C_$(BUILDTYPE))
$(OBJS): GYP_CXXFLAGS := $(DEFS_$(BUILDTYPE)) $(INCS_$(BUILDTYPE))  $(CFLAGS_$(BUILDTYPE)) $(CFLAGS_CC_$(BUILDTYPE))

# Suffix rules, putting all outputs into $(obj).

$(obj).$(TOOLSET)/$(TARGET)/%.o: $(srcdir)/%.cpp FORCE_DO_CMD
	@$(call do_cmd,cxx,1)

# Try building from generated source, too.

$(obj).$(TOOLSET)/$(TARGET)/%.o: $(obj).$(TOOLSET)/%.cpp FORCE_DO_CMD
	@$(call do_cmd,cxx,1)

$(obj).$(TOOLSET)/$(TARGET)/%.o: $(obj)/%.cpp FORCE_DO_CMD
	@$(call do_cmd,cxx,1)

# End of this set of suffix rules
### Rules for final target.
# Build our special outputs first.
$(obj).target/sipLib.so: | $(action_binding_gyp_sipLib_target_sipua_build_outputs)

# Preserve order dependency of special output on deps.
$(action_binding_gyp_sipLib_target_sipua_build_outputs): | 

LDFLAGS_Debug := \
	-pthread \
	-rdynamic \
	-m64

LDFLAGS_Release := \
	-pthread \
	-rdynamic \
	-m64

LIBS := \
	-L/root/owt-server/source/agent/sip/sipIn/sip_gateway/sipua \
	-lsipua \
	-L$(CORE_HOME)/../../build/libdeps/build/lib \
	-lre \
	-llog4cxx \
	-lboost_thread \
	-lboost_system

$(obj).target/sipLib.so: GYP_LDFLAGS := $(LDFLAGS_$(BUILDTYPE))
$(obj).target/sipLib.so: LIBS := $(LIBS)
$(obj).target/sipLib.so: LD_INPUTS := $(OBJS)
$(obj).target/sipLib.so: TOOLSET := $(TOOLSET)
$(obj).target/sipLib.so: $(OBJS) FORCE_DO_CMD
	$(call do_cmd,solink)

all_deps += $(obj).target/sipLib.so
# Add target alias
.PHONY: sipLib
sipLib: $(builddir)/sipLib.so

# Copy this to the shared library output path.
$(builddir)/sipLib.so: TOOLSET := $(TOOLSET)
$(builddir)/sipLib.so: $(obj).target/sipLib.so FORCE_DO_CMD
	$(call do_cmd,copy)

all_deps += $(builddir)/sipLib.so
# Short alias for building this shared library.
.PHONY: sipLib.so
sipLib.so: $(obj).target/sipLib.so $(builddir)/sipLib.so

# Add shared library to "all" target.
.PHONY: all
all: $(builddir)/sipLib.so
