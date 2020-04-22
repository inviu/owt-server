# This file is generated by gyp; do not edit.

TOOLSET := target
TARGET := avstream
DEFS_Debug := \
	'-DNODE_GYP_MODULE_NAME=avstream' \
	'-DUSING_UV_SHARED=1' \
	'-DUSING_V8_SHARED=1' \
	'-DV8_DEPRECATION_WARNINGS=1' \
	'-D_LARGEFILE_SOURCE' \
	'-D_FILE_OFFSET_BITS=64' \
	'-DBUILDING_NODE_EXTENSION' \
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
	-O$(OPTIMIZATION_LEVEL) \
	-g \
	-std=c++11

INCS_Debug := \
	-I/root/.cache/node-gyp/8.15.1/include/node \
	-I/root/.cache/node-gyp/8.15.1/src \
	-I/root/.cache/node-gyp/8.15.1/deps/openssl/config \
	-I/root/.cache/node-gyp/8.15.1/deps/openssl/openssl/include \
	-I/root/.cache/node-gyp/8.15.1/deps/uv/include \
	-I/root/.cache/node-gyp/8.15.1/deps/zlib \
	-I/root/.cache/node-gyp/8.15.1/deps/v8/include \
	-I$(CORE_HOME)/common \
	-I$(CORE_HOME)/owt_base \
	-I$(CORE_HOME)/../../build/libdeps/build/include

DEFS_Release := \
	'-DNODE_GYP_MODULE_NAME=avstream' \
	'-DUSING_UV_SHARED=1' \
	'-DUSING_V8_SHARED=1' \
	'-DV8_DEPRECATION_WARNINGS=1' \
	'-D_LARGEFILE_SOURCE' \
	'-D_FILE_OFFSET_BITS=64' \
	'-DBUILDING_NODE_EXTENSION'

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
	-O$(OPTIMIZATION_LEVEL) \
	-g \
	-std=c++11

INCS_Release := \
	-I/root/.cache/node-gyp/8.15.1/include/node \
	-I/root/.cache/node-gyp/8.15.1/src \
	-I/root/.cache/node-gyp/8.15.1/deps/openssl/config \
	-I/root/.cache/node-gyp/8.15.1/deps/openssl/openssl/include \
	-I/root/.cache/node-gyp/8.15.1/deps/uv/include \
	-I/root/.cache/node-gyp/8.15.1/deps/zlib \
	-I/root/.cache/node-gyp/8.15.1/deps/v8/include \
	-I$(CORE_HOME)/common \
	-I$(CORE_HOME)/owt_base \
	-I$(CORE_HOME)/../../build/libdeps/build/include

OBJS := \
	$(obj).target/$(TARGET)/addon.o \
	$(obj).target/$(TARGET)/AVStreamInWrap.o \
	$(obj).target/$(TARGET)/AVStreamOutWrap.o \
	$(obj).target/$(TARGET)/../../addons/common/NodeEventRegistry.o \
	$(obj).target/$(TARGET)/../../../core/owt_base/MediaFramePipeline.o \
	$(obj).target/$(TARGET)/../../../core/owt_base/AVStreamOut.o \
	$(obj).target/$(TARGET)/../../../core/owt_base/MediaFileOut.o \
	$(obj).target/$(TARGET)/../../../core/owt_base/LiveStreamOut.o \
	$(obj).target/$(TARGET)/../../../core/owt_base/LiveStreamIn.o

# Add to the list of files we specially track dependencies for.
all_deps += $(OBJS)

# CFLAGS et al overrides must be target-local.
# See "Target-specific Variable Values" in the GNU Make manual.
$(OBJS): TOOLSET := $(TOOLSET)
$(OBJS): GYP_CFLAGS := $(DEFS_$(BUILDTYPE)) $(INCS_$(BUILDTYPE))  $(CFLAGS_$(BUILDTYPE)) $(CFLAGS_C_$(BUILDTYPE))
$(OBJS): GYP_CXXFLAGS := $(DEFS_$(BUILDTYPE)) $(INCS_$(BUILDTYPE))  $(CFLAGS_$(BUILDTYPE)) $(CFLAGS_CC_$(BUILDTYPE))

# Suffix rules, putting all outputs into $(obj).

$(obj).$(TOOLSET)/$(TARGET)/%.o: $(srcdir)/%.cc FORCE_DO_CMD
	@$(call do_cmd,cxx,1)

$(obj).$(TOOLSET)/$(TARGET)/%.o: $(srcdir)/%.cpp FORCE_DO_CMD
	@$(call do_cmd,cxx,1)

# Try building from generated source, too.

$(obj).$(TOOLSET)/$(TARGET)/%.o: $(obj).$(TOOLSET)/%.cc FORCE_DO_CMD
	@$(call do_cmd,cxx,1)

$(obj).$(TOOLSET)/$(TARGET)/%.o: $(obj).$(TOOLSET)/%.cpp FORCE_DO_CMD
	@$(call do_cmd,cxx,1)

$(obj).$(TOOLSET)/$(TARGET)/%.o: $(obj)/%.cc FORCE_DO_CMD
	@$(call do_cmd,cxx,1)

$(obj).$(TOOLSET)/$(TARGET)/%.o: $(obj)/%.cpp FORCE_DO_CMD
	@$(call do_cmd,cxx,1)

# End of this set of suffix rules
### Rules for final target.
LDFLAGS_Debug := \
	-pthread \
	-rdynamic \
	-m64

LDFLAGS_Release := \
	-pthread \
	-rdynamic \
	-m64

LIBS := \
	-lboost_thread \
	-llog4cxx \
	-L/root/owt-server/./scripts/../build/libdeps/build//lib \
	-lavformat

$(obj).target/avstream.node: GYP_LDFLAGS := $(LDFLAGS_$(BUILDTYPE))
$(obj).target/avstream.node: LIBS := $(LIBS)
$(obj).target/avstream.node: TOOLSET := $(TOOLSET)
$(obj).target/avstream.node: $(OBJS) FORCE_DO_CMD
	$(call do_cmd,solink_module)

all_deps += $(obj).target/avstream.node
# Add target alias
.PHONY: avstream
avstream: $(builddir)/avstream.node

# Copy this to the executable output path.
$(builddir)/avstream.node: TOOLSET := $(TOOLSET)
$(builddir)/avstream.node: $(obj).target/avstream.node FORCE_DO_CMD
	$(call do_cmd,copy)

all_deps += $(builddir)/avstream.node
# Short alias for building this executable.
.PHONY: avstream.node
avstream.node: $(obj).target/avstream.node $(builddir)/avstream.node

# Add executable to "all" target.
.PHONY: all
all: $(builddir)/avstream.node
